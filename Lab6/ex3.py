import matplotlib.pyplot as plt
import numpy as np
import scipy

def rectangleWindow(size):
    return np.zeros(size) + 1

def HanningWindow(size):
    window = np.zeros(size)
    for i in range(size):
        window[i] = 1 - np.cos(2 * np.pi * i / size)
    return window / 2

def sinusodialSignal(time):
    return np.sin(2 * np.pi * 100 * time)

samples = np.linspace(0, 1, 200)
y = sinusodialSignal(samples)

window1 = rectangleWindow(200)
window2 = HanningWindow(200)

y1 = y * window1
y2 = y * window2

fig, axs = plt.subplots(3)

axs[0].plot(samples, y)
axs[1].plot(samples, y1)
axs[2].plot(samples, y2)

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')


plt.savefig('ex3.png', format='png')
plt.savefig('ex3.pdf', format='pdf')