import numpy as np
from scipy.io import wavfile
from scipy.signal import stft
import matplotlib.pyplot as plt

fs, data = wavfile.read('./gamchan/media/sample.wav')

t = np.arange(len(data)) / fs

frequencies, times, Zxx = stft(data, fs)
Zxx_db = 20 * np.log10(np.abs(Zxx))
vmin = Zxx_db.max() - 80
vmax = Zxx_db.max()

plt.pcolormesh(
    times, 
    frequencies,
    Zxx_db, 
    vmin=vmin, vmax=vmax, 
    shading='gouraud'
)
plt.xlabel('Time[sec]')
plt.xlim([0, 5])
plt.ylabel('Freq[Hz]')
plt.title('stft')
plt.colorbar(label='Magnitude[dB]')
plt.savefig('./gamchan/media/stft.png')