from scipy.io.wavfile import read
import numpy as np

def readAudio(fName):
    fs,data=read(fName)
    print(type(data[0]))
    if np.issubdtype(data.dtype,np.integer):
        max=np.max(np.fabs(data))
        data=data.astype(float)/max
    return fs,data
