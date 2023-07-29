import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft
import matplotlib.pyplot as plt

fs, data = wavfile.read('./gamchan/media/sample.wav')

t = np.arange(len(data)) / fs

yf = fft(data)
xf = np.fft.fftfreq(len(yf), 1/fs)

plt.figure(figsize=(10, 4))
plt.plot(xf, 2.0/len(data) * np.abs(yf))
plt.xlabel('Freq[Hz]')
plt.xlim([0, fs/2])
plt.ylabel('Magnitude')
plt.title('fft')
plt.savefig('./gamchan/media/fft.png')