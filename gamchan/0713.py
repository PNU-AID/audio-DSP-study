import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft
from scipy.signal import stft
import matplotlib.pyplot as plt

fs, data = wavfile.read('./gamchan/audio/sample.wav')

t = np.arange(len(data)) / fs

plt.figure(figsize=(10, 4))
plt.plot(t, data)
plt.xlabel('t')
plt.xlim([0, 5])
plt.ylabel('f')
plt.title('wav file')
plt.show()

yf = fft(data)
xf = np.linspace(0.0, fs/2, len(yf))

plt.figure(figsize=(10, 4))
plt.plot(xf, 2.0/len(data) * np.abs(yf))
plt.xlabel('t')
plt.xlim([0, 5])
plt.ylabel('f')
plt.title('fft')
plt.show()

frequencies, times, Zxx = stft(data, fs)
plt.pcolormesh(times, frequencies, 20*np.log10(np.abs(Zxx)), vmin=0, vmax=1, shading='gouraud')
plt.xlabel('t')
plt.xlim([0, 5])
plt.ylabel('f')
plt.title('stft')
plt.show()
