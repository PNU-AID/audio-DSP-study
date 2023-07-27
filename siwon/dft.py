import numpy as np
import matplotlib.pyplot as plt
import wavegen

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
        #Create Window
        self.wFuncX=np.arange(self.point) #Create X Axis Array
        #Blackman Window
        wAlpha=0.16
        self.wBlackman=(1-wAlpha)/2-0.5*np.cos((2*np.pi/self.point)*self.wFuncX)+(wAlpha/2)*np.cos((4*np.pi/self.point)*self.wFuncX)
        #Hann Window
        self.wHann=np.power(np.sin(np.pi/self.point*self.wFuncX),2)

    def rectWindow(self,data,start):
        return data[start:start+self.point]
    
    def blackmanWindow(self,data,start):
        out=data[start:start+self.point]*self.wBlackman
        return out
    
    def hannWindow(self,data,start):
        out=data[start:start+self.point]*self.wHann
        return out
    
    def dftSingle(self,data,start,window):
        if window=='rect':
            d=self.rectWindow(data,start)
        elif window=='blackman':
            d=self.blackmanWindow(data,start)
        elif window=='hann':
            d=self.hannWindow(data,start)
        else:
            raise ValueError('Undefined Window Type')
        return np.dot(self.convArray,d)[0:int(self.point/2)]

    def convertMag(self,data,window,overlap,logscale=0):
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
        #Normalize Result
        result=result/np.max(result)
        #Convert to log
        if logscale:
            result=20*np.log10(result)
        return time,result
    
    def addPadding(self,data):
        diff=data.size%self.point
        if diff == 0:
            return data
        else:
            return np.pad(data,(0,diff))