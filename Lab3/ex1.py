import math
import numpy as np
import matplotlib.pyplot as plt

FourierMatrix = [[0 for i in range(8)] for i in range(8)]

for i in range(8):
    for j in range(8):
        FourierMatrix[i][j] = math.e**(-2 * np.pi * 1j * i * j / 8)

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
    
    plt.savefig(f'Ex1_linia{i}.pdf', format='pdf')
    plt.savefig(f'Ex1_linia{i}.png', format='png')
    
    plt.show()
        
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
        