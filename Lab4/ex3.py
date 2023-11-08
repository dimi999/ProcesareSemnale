import numpy as np
import matplotlib.pyplot as plt
import math
import time
import win_precise_time as wpt

def sinusoidalSignal(time):
    return np.sin(2 * np.pi * 5 * time)

def otherSignal1(time):
    return np.sin(2 * np.pi * 11 * time)

def otherSignal2(time):
    return np.sin(2 * np.pi * 17 * time)

samples = np.linspace(0, 1, 15)
values = sinusoidalSignal(samples)

samplesSignal = np.linspace(0, 1, 1000)

values1 = otherSignal1(samplesSignal)
values2 = otherSignal2(samplesSignal)

fig, axs = plt.subplots(3)
fig.suptitle('Exercitiul 3')
axs[0].stem(samples, values)
axs[1].stem(samples, values)
axs[1].plot(samplesSignal, values1, color='red')
axs[2].stem(samples, values)
axs[2].plot(samplesSignal, values2, color='red')

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')
    
plt.savefig('ex3.pdf', format='pdf')
plt.savefig('ex3.png', format='png')