import matplotlib.pyplot as plt
import numpy as np
import scipy
import sounddevice

def sinusoidalSignal1(time):
    return np.sin(1500 * time)

def sinusoidalSignal2(time):
    return np.sin(3000 * time)

samples = np.linspace(0, 1, 2000)


values1 = sinusoidalSignal1(samples)
values2 = sinusoidalSignal2(samples)
values3 = np.concatenate([values1, values2])

fig, axs = plt.subplots(2)
fig.suptitle('Exercitiul 5')
axs[0].plot(samples[:200], values1[:200])
axs[1].plot(samples[:200], values2[:200])

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')

plt.savefig('Ex5.pdf', format='pdf')

sounddevice.play(values3, 2000)
sounddevice.wait()