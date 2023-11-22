import matplotlib.pyplot as plt
import numpy as np
import scipy

x = np.random.rand(200) * 50
y = np.random.rand(200) * 50

for i in range(100, 200):
    x[i] = y[i] = 0

z = np.zeros(200)

for i in range(100):
    for j in range(100):
        z[i + j] += x[i] * y[j]

xfft = np.fft.fft(x)
yfft = np.fft.fft(y)
zfft = xfft * yfft

znormalfft = np.fft.ifft(zfft)

for i in range(199):
    print(abs(znormalfft[i] - z[i]))