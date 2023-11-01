import math
import numpy as np
import matplotlib.pyplot as plt

def signal1(time):
    return np.cos(2 * np.pi * 3 * time)

def signal2(time):
    return 2 * np.cos(2 * np.pi * 7 * time)

def signal3(time):
    return 0.5 * np.cos(2 * np.pi * 15 * time)
    
#Doar pt plotul original
samples = np.linspace(0, 1, 2000)
values = signal1(samples) + signal2(samples) - signal3(samples)
plt.plot(samples, values)
plt.savefig('Ex3_semnal.pdf', format='pdf')
plt.savefig('Ex3_semnal.png', format='png')
plt.figure()

#De aici incepe exercitiul efectiv
samples = np.linspace(0, 1, 101) 
#linspaceul ne pune ambele capete in sample, daca esantionam 100 de valori am fi avut leakege
values = signal1(samples) + signal2(samples) - signal3(samples)

FourierMatrix = np.matrix(np.zeros((100, 100)), dtype=complex)
for i in range(100):
    for j in range(100):
        FourierMatrix[i,j] = math.e**(-2 * np.pi * 1j * i * j / 100)

X = np.dot(FourierMatrix, values.T[:100])
print(X.shape)

plt.stem([i for i in range(100)], [abs(X[0, i]) for i in range(100)])

plt.savefig('Ex3_Fourier.pdf', format='pdf')
plt.savefig('Ex3_Fourier.png', format='png')