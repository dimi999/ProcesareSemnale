import matplotlib.pyplot as plt
import numpy as np


def x(time):
    return np.cos(520 * np.pi * time + np.pi / 3)

def y(time):
    return np.cos(280 * np.pi * time - np.pi / 3)

def z(time):
    return np.cos(120 * np.pi * time + np.pi / 3)

samples = np.linspace(0, 0.03, 2000)
valuesX = x(samples)
valuesY = y(samples)
valuesZ = z(samples)

fig, axs = plt.subplots(3)
fig.suptitle('Exercitiul 1 b')
axs[0].stem(samples, valuesX)
axs[1].stem(samples, valuesY)
axs[2].stem(samples, valuesZ)

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')
    ax.set_ylim([-1, 1])


plt.savefig('ex1b.pdf', format='pdf')
plt.show()
plt.close()

samples200HZ = np.linspace(0, 0.05, 10)
samplesFunction = np.linspace(0, 0.05, 200)
valuesX = x(samples200HZ)
valuesFunctionX = x(samplesFunction)
valuesY = y(samples200HZ)
valuesFunctionY = y(samplesFunction)
valuesZ = z(samples200HZ)
valuesFunctionZ = z(samplesFunction)

fig, axs = plt.subplots(3)
fig.suptitle('Exercitiul 1 c')
axs[0].stem(samples200HZ, valuesX)
axs[0].plot(samplesFunction, valuesFunctionX, color='red')
axs[1].stem(samples200HZ, valuesY)
axs[1].plot(samplesFunction, valuesFunctionY, color='red')
axs[2].stem(samples200HZ, valuesZ)
axs[2].plot(samplesFunction, valuesFunctionZ, color='red')

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')
    ax.set_ylim([-1, 1])

plt.savefig('ex1c.pdf', format='pdf')
plt.show()
plt.close()



 