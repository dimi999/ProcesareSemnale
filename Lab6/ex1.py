import matplotlib.pyplot as plt
import numpy as np
import scipy

x = np.random.rand(100) * 50

fig, axs = plt.subplots(4)
axs[0].plot(x)
x = np.convolve(x, x)
axs[1].plot(x)
x = np.convolve(x, x)
axs[2].plot(x)
x = np.convolve(x, x)
axs[3].plot(x)

for ax in axs.flat:
    ax.set_xlabel('indice')
    ax.set_ylabel('valoare')

plt.savefig('ex1.png', format='png')
plt.savefig('ex1.pdf', format='pdf')