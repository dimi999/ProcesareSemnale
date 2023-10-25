import matplotlib.pyplot as plt
import numpy as np
import scipy
import sounddevice

def sinSignal(time):
    return 0.5 * np.sin(200 * time)

def cosSignal(time):
    return 0.5 * np.cos(200 * time - np.pi / 2)

samples = np.linspace(0, 1, 2000)

values1 = sinSignal(samples)
values2 = cosSignal(samples)

#plt.plot(samples, values1)
#plt.figure()
#plt.plot(samples, values2)
#plt.figure()

fig, axs = plt.subplots(2)
fig.suptitle('Exercitiul 1, sus semnal generat cu sin, jos cu cos')
axs[0].plot(samples, values1)
axs[1].plot(samples, values2)

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')
    
plt.savefig('Ex1.pdf', format='pdf')    
