import numpy as np
import matplotlib.pyplot as plt
import wavegen
from dft import DFT

sampleRate=5000 #40000Hz-> Bandwidth=20KHz
transformPoint=256

DFT1024=DFT(transformPoint,sampleRate)
dataX=np.arange(0,1,1/sampleRate)
#Generate Sample Data
#dataY=generateSine(1,10000,sampleRate)+generateSine(1,5000,sampleRate)*5
#dataY=wavegen.generateSquare(1,1000,sampleRate)
dataY=wavegen.generateSweep(1,100,2000,sampleRate)
#Convert
time,result=DFT1024.convertMag(dataY,'blackman',128)
#Draw Plot
resultX=np.arange(0,sampleRate/2,sampleRate/transformPoint)
#plt.plot(resultX,result[0:int(transformPoint/2)])
plt.figure(figsize=(5,5))
plt.pcolormesh(resultX,time,result,shading='gouraud')
plt.show()