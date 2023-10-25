import matplotlib.pyplot as plt
import numpy as np
import scipy
import sounddevice

def sinSignal1(time):
    return np.sin(50 * 2 * np.pi * time)

def sinSignal2(time):
    return np.sin(25 * 2 * np.pi * time)

def sinSignal0(time):
    return np.sin(0 * 2 * np.pi * time)

samples = np.linspace(0, 1, 100)
values1 = sinSignal1(samples)
values2 = sinSignal2(samples)
values3 = sinSignal0(samples)

fig, axs = plt.subplots(3)
fig.suptitle('Exercitiul 6')
axs[0].plot(samples, values1)
axs[1].plot(samples, values2)
axs[2].plot(samples, values3)

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')
    
plt.savefig('Ex6.pdf', format='pdf')