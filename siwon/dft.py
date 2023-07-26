import numpy as np
import matplotlib.pyplot as plt
import wavegen

sampleRate=5000 #40000Hz-> Bandwidth=20KHz
transformPoint=256

class DFT:
    def __init__(self,point,samplerate):
        self.point=point
        self.samplerate=samplerate
        #Create DFT Array
        w=np.exp((-2*np.pi*1j)/self.point)
        self.convArray=np.full([self.point,self.point],w)
        multiplier=np.zeros([self.point,self.point])
        for i in range(self.point):
            for j in range(self.point):
                multiplier[i][j]=i*j
        self.convArray=np.power(self.convArray,multiplier)/np.sqrt(self.point)

    def rectWindow(self,data,start):
        return data[start:start+self.point]
    
    def blackmanWindow(self,data,start):
        funcX=np.arange(self.point)
        alpha=0.16
        funcY=(1-alpha)/2-0.5*np.cos((2*np.pi/self.point)*funcX)+(alpha/2)*np.cos((4*np.pi/self.point)*funcX)
        out=data[start:start+self.point]*funcY
        return out
    
    def hannWindow(self,data,start):
        funcX=np.arange(self.point)
        funcY=np.power(np.sin(np.pi/self.point*funcX),2)
        out=data[start:start+self.point]*funcY
        return out
    
    def dftSingle(self,data,start,window):
        if window=='rect':
            d=self.rectWindow(data,start)
        elif window=='blackman':
            d=self.blackmanWindow(data,start)
        elif window=='hann':
            d=self.hannWindow(data,start)
        return np.dot(self.convArray,d)[0:int(self.point/2)]

    def convertMag(self,data,window,overlap):
        time=np.array([])
        result=np.array([])
        #Add Padding to data
        data=self.addPadding(data)
        #Conversion
        for i in range(0,data.size-self.point,self.point-overlap):
            time=np.append(time,1/self.samplerate*i)
            resultSingle=np.absolute(self.dftSingle(data,i,window))
            result=np.append(result,resultSingle)
        #Reshape Flattened Array
        result=np.reshape(result,(-1,int(self.point/2)))
        return time,result
    
    def addPadding(self,data):
        diff=data.size%self.point
        if diff == 0:
            return data
        else:
            return np.pad(data,(0,diff))

    
    

DFT1024=DFT(transformPoint,sampleRate)
dataX=np.arange(0,1,1/sampleRate)
#Generate Sample Data
#dataY=generateSine(1,10000,sampleRate)+generateSine(1,5000,sampleRate)*5
#dataY=wavegen.generateSquare(1,1000,sampleRate)
dataY=wavegen.generateSweep(1,100,2000,sampleRate)
#Convert
time,result=DFT1024.convertMag(dataY,'hann',128)
#Draw Plot
resultX=np.arange(0,sampleRate/2,sampleRate/transformPoint)
#plt.plot(resultX,result[0:int(transformPoint/2)])
plt.figure(figsize=(12,5))
plt.pcolormesh(resultX,time,result,shading='flat')
plt.show()