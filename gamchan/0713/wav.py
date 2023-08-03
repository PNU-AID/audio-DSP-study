import numpy as np
from scipy.io import wavfile
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

fs, data = wavfile.read('./gamchan/media/sample.wav')

t = np.arange(len(data)) / fs

floor = 1e-10
data_db = 20 * np.log10(np.abs(data + floor) / np.max(np.abs(data + floor)))

plt.figure(figsize=(10, 4))
plt.plot(t, data)
plt.xlabel('t[sec]')
plt.xlim([0, 5])
plt.ylabel('Amplitude[dB]')
plt.title('wav file')
plt.savefig('./gamchan/media/wav_file.png')