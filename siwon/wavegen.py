import numpy as np
from scipy import signal

def generateSine(duration,freq,sample):
    x=np.arange(0,duration,1/sample)
    y=np.sin(2*np.pi*freq*x)
    return y

def generateSquare(duration,freq,sample,high=1,low=-1):
    x=np.arange(0,duration,1/sample)
    y=signal.square(2*np.pi*freq*x)*(high-low)/2+(high-low)/2+low
    return y