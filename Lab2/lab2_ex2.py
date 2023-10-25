import matplotlib.pyplot as plt
import numpy as np
import scipy
import sounddevice

samples = np.linspace(0, 1, 2000)

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

plt.xlabel('timp')
plt.ylabel('amplitudine')

plt.plot(samples, values1, color='red')
plt.plot(samples, values2, color='blue')
plt.plot(samples, values3, color='green')
plt.plot(samples, values4, color='yellow')

plt.savefig('Ex2a.pdf', format='pdf')

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

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')

plt.savefig('Ex2b.pdf', format='pdf')