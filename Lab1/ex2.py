import matplotlib.pyplot as plt
import numpy as np

def sinusoidalSignal(time):
    return 0.5 * np.sin(400 * time)

def sinusoidalSignal2(time):
    return np.sin(800 * time)

samples = np.linspace(0, 1, 1600)
samples2 = np.linspace(0, 3, 200)
values = sinusoidalSignal(samples)
values2 = sinusoidalSignal2(samples2)

fig, axs = plt.subplots(2)
fig.suptitle('Exercitiul 2 a, b')
axs[0].plot(samples, values)
axs[1].plot(samples2, values2)

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')
    ax.set_ylim([-1, 1])

plt.savefig('Ex2ab.pdf', format='pdf')
plt.show() 

def sawtooth(time):
    return 2 * (240 * time - np.floor(240 * time)) - 1

def square(time):
    return np.sign(np.sin(2 * np.pi * 300 * time))

samples = np.linspace(0, 0.05, 2000)
values = sawtooth(samples)
values2 = square(samples)

fig, axs = plt.subplots(2)
fig.suptitle('Exercitiul 2 c, d')
axs[0].plot(samples, values)
axs[1].plot(samples, values2)

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')
    ax.set_ylim([-1.2, 1.2])

plt.savefig('Ex2cd.pdf', format='pdf')
plt.show() 

matrix = np.random.rand(128, 128)
plt.imshow(matrix)
plt.suptitle('Semnal Random')
plt.savefig('Ex2e.pdf', format='pdf')
plt.show()

def init(i, j):
    return np.sin(i * i) * np.sin(j * j)

matrix2 = np.fromfunction(init, (128, 128))
plt.imshow(matrix2)
plt.suptitle('Semnal generat cu formula')
plt.savefig('Ex2f.pdf', format='pdf')
plt.show()