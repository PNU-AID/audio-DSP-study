import numpy as np
import matplotlib.pyplot as plt
import wavegen

sampleRate=40000 #40000Hz-> Bandwidth=20KHz
transformPoint=1024

class DFT:
    def __init__(self,point):
        self.point=point
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

    def convertMag(self,data,window):
        if window=='rect':
            d=self.rectWindow(data,0)
        elif window=='blackman':
            d=self.blackmanWindow(data,0)
        elif window=='hann':
            d=self.hannWindow(data,0)
        return np.absolute(np.dot(self.convArray,d))
    

DFT1024=DFT(transformPoint)
dataX=np.arange(0,1,1/sampleRate)
#dataY=generateSine(1,10000,sampleRate)+generateSine(1,5000,sampleRate)*5
dataY=wavegen.generateSquare(1,2500,sampleRate)
result=DFT1024.convertMag(dataY,'rect')
resultX=np.arange(0,sampleRate/2,sampleRate/transformPoint)
plt.plot(resultX,result[0:int(transformPoint/2)])
plt.show()