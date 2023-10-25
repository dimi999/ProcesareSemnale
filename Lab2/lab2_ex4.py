import matplotlib.pyplot as plt
import numpy as np
import scipy
import sounddevice

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

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')

plt.savefig('Ex4.pdf', format='pdf')

sounddevice.play(values3, 2000)
sounddevice.wait()