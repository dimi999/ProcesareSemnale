import math
import numpy as np
import matplotlib.pyplot as plt

FourierMatrix = [[0 for i in range(8)] for i in range(8)]

for i in range(8):
    for j in range(8):
        FourierMatrix[i][j] = math.e**(2 * np.pi * 1j * i * j / 8)

#print(FourierMatrix)

samples = [0, 1, 2, 3, 4, 5, 6, 7]
real = [0, 0, 0, 0, 0, 0, 0, 0]
imaginary = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(8):
    for j in range(8):
        real[j] = FourierMatrix[i][j].real
        imaginary[j] = FourierMatrix[i][j].imag
        
    fig, axs = plt.subplots(2)
    fig.suptitle(f'Linia {i}')
    axs[0].stem(samples, real)
    axs[1].stem(samples, imaginary)
        
    for ax in axs.flat:
        ax.set_xlabel('linia')
        ax.set_ylabel('coloana')

FourierMatrix = np.matrix(FourierMatrix)
FourierConj = 1/8 * np.conj(np.transpose(FourierMatrix))

ErrorMatrix = np.dot(FourierMatrix, FourierConj) - np.identity(8)
ErrorMatrix = np.abs(ErrorMatrix)
EPS = 0.0000000001

for i in range(8):
    for j in range(8):
        if ErrorMatrix[i,j] > EPS:
            print("Matrice neunitara")
            

#%%EX 2

def sinusoidalSignal(time):
    return np.sin(time * 3 * np.pi * 2)

count = 1200
samples = np.linspace(0, 1, count)
values = sinusoidalSignal(samples)

omega = [1, 3, 99, 15]
imaginary1 = [values[j] * math.e**(-2 * np.pi * 1j * omega[0] * j / 400) for j in range(count)]
imaginary2 = [values[j] * math.e**(-2 * np.pi * 1j * omega[1] * j / 400) for j in range(count)]
imaginary3 = [values[j] * math.e**(-2 * np.pi * 1j * omega[2] * j / 400) for j in range(count)]
imaginary4 = [values[j] * math.e**(-2 * np.pi * 1j * omega[3] * j / 400) for j in range(count)]

imaginary1 = np.array(imaginary1)
imaginary2 = np.array(imaginary2)
imaginary3 = np.array(imaginary3)
imaginary4 = np.array(imaginary4)

fig, axs = plt.subplots(2)
fig.suptitle('Exercitiul2') 
axs[0].plot(samples, values)
axs[1].plot(imaginary1.real, imaginary1.imag)
plt.figure()

plt.plot(imaginary2.real, imaginary2.imag)
plt.figure()
plt.plot(imaginary3.real, imaginary3.imag)
plt.figure()
plt.plot(imaginary4.real, imaginary4.imag)

            



