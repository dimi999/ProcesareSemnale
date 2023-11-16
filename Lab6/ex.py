import matplotlib.pyplot as plt
import numpy as np
import scipy

#%% Ex1
x = np.random.rand(100) * 50

plt.plot(x)
plt.figure()

x = np.convolve(x, x)
plt.plot(x)
plt.figure()

x = np.convolve(x, x)
plt.plot(x)
plt.figure()

x = np.convolve(x, x)
plt.plot(x)
plt.figure()

#%% Ex2

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
    
#%% Ex3

def rectangleWindow(size):
    return np.zeros(size) + 1

def HanningWindow(size):
    window = np.zeros(size)
    for i in range(size):
        window[i] = 1 - np.cos(2 * np.pi * i / size)
    return window / 2

def sinusodialSignal(time):
    return np.sin(2 * np.pi * 100 * time)

samples = np.linspace(0, 1, 200)
y = sinusodialSignal(samples)
plt.plot(samples, y)
plt.figure()

window1 = rectangleWindow(200)
window2 = HanningWindow(200)

y1 = y * window1
y2 = y * window2

plt.plot(samples, y1)
plt.figure()
plt.plot(samples, y2)
plt.figure()

#%% Ex4

x = np.genfromtxt('D:/procesareSemnale/Lab6/Train.csv', delimiter=',')

vals = x[:,2]
vals = vals[1 : 73]

print(len(vals))

avgs = [5, 9, 13, 17]
for w in avgs:
    avg = np.convolve(vals, np.ones(w), 'valid') / w
    print(len(avg))

