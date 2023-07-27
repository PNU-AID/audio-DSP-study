from scipy.io.wavfile import read
import numpy as np

def readAudio(fName):
    fs,data=read(fName)
    if data.ndim==2:
        dataMono=(data[:,0]/2)+(data[:,1]/2)
        max=np.max(np.fabs(dataMono))
        dataMono=dataMono.astype(float)/max
        return fs,dataMono
    if np.issubdtype(data.dtype,np.integer):
        max=np.max(np.fabs(data))
        data=data.astype(float)/max
    return fs,data
