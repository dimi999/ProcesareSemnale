import numpy as np
import matplotlib.pyplot as plt
import math
import time
import win_precise_time as wpt

import scipy

rate, x = scipy.io.wavfile.read('D:/procesareSemnale/Lab4/vocale.wav')
groups = []

for i in range(0, len(x), len(x) // 200):
    group = []
    for j in range(i, min(len(x), i + len(x) // 100)):
        group.append(x[j])
    groups.append(group)

ffts = []
for group in groups:
    values = np.array(group)
    fftValues = np.fft.fft(values)
    ffts.append(fftValues)
    
imag = np.zeros((len(groups), len(groups[0])))
for i in range(len(ffts)):
    for j in range(len(ffts[i])):
        imag[i][j] = abs(ffts[i][j])

imag = imag.T

plt.imshow(imag, norm='symlog', aspect=0.05, cmap='inferno')
plt.savefig('ex6.pdf', format='pdf')
plt.savefig('ex6.png', format='png')