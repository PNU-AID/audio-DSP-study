import audioread
import numpy as np
import matplotlib.pyplot as plt
from dft import DFT
from audioread import readAudio

sampleRate,audioData=readAudio('siwon/sample.wav')
print('Sample Rate: '+str(sampleRate))
windowSize=512
dft=DFT(windowSize,sampleRate)
#timeAxis=np.arange(audioData.size)/sampleRate
#Execute STFT Conversion
freqAxis=np.arange(0,sampleRate/2,sampleRate/windowSize)
timeAxis,result=dft.convertMag(audioData,'hann',256,1)
#Draw Plot
plt.figure(figsize=(5,5))
plt.pcolormesh(freqAxis,timeAxis,result,shading='gouraud',cmap='magma')
plt.show()