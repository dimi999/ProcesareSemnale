import matplotlib.pyplot as plt
import numpy as np
import scipy
import sounddevice

#rate = int(10e5)
#fs = 44100
#signal = np.random.randint(0, 100, fs)
#signal = np.sin(signal)

#scipy.io.wavfile.write('nume.wav', rate, signal)
#rate, signal = scipy.io.wavfile.read('nume.wav')

#sounddevice.play(signal, fs)
#sounddevice.wait()

def sinSignal(time):
    return 0.5 * np.sin(200 * time)

def cosSignal(time):
    return 0.5 * np.cos(200 * time - np.pi / 2)

samples = np.linspace(0, 1, 2000)

values1 = sinSignal(samples)
values2 = cosSignal(samples)

plt.plot(samples, values1)
plt.figure()
plt.plot(samples, values2)
plt.figure()

def sinSignal1(time):
    return np.sin(40 * time + np.pi / 12)

def sinSignal2(time):
    return np.sin(40 * time - np.pi / 7)

def sinSignal3(time):
    return np.sin(40 * time + np.pi / 3)

def sinSignal4(time):
    return np.sin(40 * time - np.pi / 2)

values1 = sinSignal1(samples)
values2 = sinSignal2(samples)
values3 = sinSignal3(samples)
values4 = sinSignal4(samples)

plt.plot(samples, values1, color='red')
plt.plot(samples, values2, color='blue')
plt.plot(samples, values3, color='green')
plt.plot(samples, values4, color='yellow')

plt.figure()

noise = np.random.normal(0, 1, 2000)
norma_z = np.linalg.norm(noise)
    
values1 = sinSignal1(samples)
norma1 = np.linalg.norm(values1)
param1 = np.sqrt(norma1 / norma_z / 0.1)
values1 = values1 + param1 * noise

values2 = sinSignal1(samples)
norma2 = np.linalg.norm(values2)
param2 = np.sqrt(norma2 / norma_z / 1)
values2 = values2 + param2 * noise

values3 = sinSignal1(samples)
norma3 = np.linalg.norm(values3)
param3 = np.sqrt(norma3 / norma_z / 10)
values3 = values3 + param3 * noise

values4 = sinSignal1(samples)
norma4 = np.linalg.norm(values4)
param4 = np.sqrt(norma4 / norma_z / 100)
values4 = values4 + param4 * noise

fig, axs = plt.subplots(4)
fig.suptitle('Exercitiul 2')
axs[0].plot(samples, values1)
axs[1].plot(samples, values2)
axs[2].plot(samples, values3)
axs[3].plot(samples, values4)


rate1, x1 = scipy.io.wavfile.read('../lab1/semnal2a.wav')
rate2, x2 = scipy.io.wavfile.read('../lab1/semnal2b.wav')
rate3, x3 = scipy.io.wavfile.read('../lab1/semnal2c.wav')
rate4, x4 = scipy.io.wavfile.read('../lab1/semnal2d.wav')

sounddevice.play(x1, rate1)
sounddevice.wait()
sounddevice.play(x2, rate2)
sounddevice.wait()
sounddevice.play(x3, rate3)
sounddevice.wait()
sounddevice.play(x4, rate4)
sounddevice.wait()

def sawtooth(time):
    return 2 * (80 * time - np.floor(80 * time)) - 1

def square(time):
    return np.sign(np.sin(2 * np.pi * 50 * time))

samples = np.linspace(0, 1, 2000)

values1 = sawtooth(samples)
values2 = square(samples)
values3 = values1 + values2

fig, axs = plt.subplots(3)
fig.suptitle('Exercitiul 4')
axs[0].plot(samples, values1)
axs[1].plot(samples, values2)
axs[2].plot(samples, values3)

sounddevice.play(values3, 2000)
sounddevice.wait()

def sinusoidalSignal1(time):
    return np.sin(1500 * time)

def sinusoidalSignal2(time):
    return np.sin(3000 * time)

values1 = sinusoidalSignal1(samples)
values2 = sinusoidalSignal2(samples)
values3 = np.concatenate([values1, values2])

plt.show()

fig, axs = plt.subplots(2)
fig.suptitle('Exercitiul 5')
axs[0].plot(samples, values1)
axs[1].plot(samples, values2)

sounddevice.play(values3, 2000)
sounddevice.wait()

plt.show()
