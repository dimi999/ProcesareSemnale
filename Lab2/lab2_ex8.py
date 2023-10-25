import matplotlib.pyplot as plt
import numpy as np
import scipy

def PadeAproximation(x):
    return (x - 7 * x**3 / 60) / (1 + x*x / 20)

samples = np.linspace(-np.pi / 2, np.pi / 2, 1000)
values1 = np.sin(samples)
values2 = samples
values3 = PadeAproximation(samples)
values4 = abs(values1 - values2)
values5 = abs(values1 - values3)

fig, axs = plt.subplots(5)
fig.suptitle('Ex 8a, SIN X, X, PADE(X), ERR(SIN X, X), ERR(SIN X, PADE(X))')
axs[0].plot(samples, values1)
axs[1].plot(samples, values2)
axs[2].plot(samples, values3)
axs[3].plot(samples, values4)
axs[4].plot(samples, values5)

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('eroare')

plt.savefig('Ex8a.pdf', format='pdf')

plt.show()

values4 = np.log(abs(values1 - values2))
values5 = np.log(abs(values1 - values3))

fig, axs = plt.subplots(2)
fig.suptitle('Ex 8b, Eroarea pe axa OY logaritimica')
axs[0].plot(samples, values4)
axs[1].plot(samples, values5)

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('lg(eroare)')

plt.savefig('Ex8b.pdf', format='pdf')
plt.show()