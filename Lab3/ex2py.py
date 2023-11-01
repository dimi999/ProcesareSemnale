import math
import numpy as np
import matplotlib.pyplot as plt

def sinusoidalSignal(time):
    return np.sin(time * 3 * np.pi * 2)

count = 2500
samples = np.linspace(0, 1, count)
values = sinusoidalSignal(samples)

omega = [1, 3, 10, 15]
imaginary1 = [values[j] * math.e**(-2 * np.pi * 1j * omega[0] * j / count) for j in range(count)]
imaginary2 = [values[j] * math.e**(-2 * np.pi * 1j * omega[1] * j / count) for j in range(count)]
imaginary3 = [values[j] * math.e**(-2 * np.pi * 1j * omega[2] * j / count) for j in range(count)]
imaginary4 = [values[j] * math.e**(-2 * np.pi * 1j * omega[3] * j / count) for j in range(count)]

imaginary1 = np.array(imaginary1)
imaginary2 = np.array(imaginary2)
imaginary3 = np.array(imaginary3)
imaginary4 = np.array(imaginary4)

plt.plot(samples, values)
plt.savefig('Ex2_semnal.pdf', format='pdf')
plt.savefig('Ex2_semnal.png', format='png')


fig, axs = plt.subplots(2, 2)
fig.suptitle('Exercitiul2\n omega=1, 3, 10, 15') 
axs[0,0].scatter(imaginary1.real, imaginary1.imag, c=abs(imaginary1), cmap='RdYlBu')
axs[0,1].scatter(imaginary2.real, imaginary2.imag, c=abs(imaginary2), cmap='RdYlBu')
axs[1,0].scatter(imaginary3.real, imaginary3.imag, c=abs(imaginary3), cmap='RdYlBu')
axs[1,1].scatter(imaginary4.real, imaginary4.imag, c=abs(imaginary4), cmap='RdYlBu')

for ax in axs.flat:
    ax.set_xlabel('real')
    ax.set_ylabel('imaginar')

plt.savefig('Ex2_plan_complex.pdf', format='pdf')
plt.savefig('Ex2_plan_complex.png', format='png')
plt.show()