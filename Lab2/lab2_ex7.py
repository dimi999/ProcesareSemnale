import matplotlib.pyplot as plt
import numpy as np
import scipy

def sinusoidalSignal(time):
    return np.sin(100 * time * np.pi * 2 + np.pi / 4)

samples = np.linspace(0, 0.2, 200)
values = sinusoidalSignal(samples)

fig, axs = plt.subplots(3)
fig.suptitle('Exercitiul 7ab')
axs[0].plot(samples, values)
axs[1].plot(samples[::4], values[::4])
axs[2].plot(samples[1::4], values[1::4])

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')

plt.savefig('Ex7.pdf', format='pdf')

