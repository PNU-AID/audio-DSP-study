import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

def generateSine(duration,freq,sample):
    x=np.arange(0,duration,1/sample)
    y=np.sin(2*np.pi*freq*x)
    return y

def generateSquare(duration,freq,sample,high=1,low=-1):
    x=np.arange(0,duration,1/sample)
    y=signal.square(2*np.pi*freq*x)*(high-low)/2+(high-low)/2+low
    return y

def generateSweep(duration,fStart,fEnd,sample):
    x=np.arange(0,duration,1/sample)
    y=signal.chirp(x,fStart,x[x.size-1],fEnd)
    return y