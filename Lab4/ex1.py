import numpy as np
import matplotlib.pyplot as plt
import math
import time
import win_precise_time as wpt

def signal1(time):
    return np.cos(2 * np.pi * 3 * time)

def signal2(time):
    return 2 * np.cos(2 * np.pi * 7 * time)

def signal3(time):
    return 0.5 * np.cos(2 * np.pi * 15 * time)
    
dimensiuni = [128, 256, 512, 1024, 2048, 4096, 8192]
dimensiuniNP = [16384]
timpPersonal = []
timpNP = []

for dim in dimensiuni:
    
    samples = np.linspace(0, 1, dim + 1) 
    values = signal1(samples) + signal2(samples) - signal3(samples)
    
    initTime = wpt.time()
    
    FourierMatrix = np.matrix(np.zeros((dim, dim)), dtype=complex)
    for i in range(dim):
        for j in range(dim):
            FourierMatrix[i,j] = math.e**(-2 * np.pi * 1j * i * j / dim)
    
    X = np.dot(FourierMatrix, values.T[:dim])
    
    finishTime = wpt.time()
    
    initTimenp = wpt.time()
    
    X = np.fft.fft(values[:dim])
    
    finalTimenp = wpt.time()
    
    timpPersonal.append(finishTime - initTime)
    timpNP.append(finalTimenp - initTimenp)

for i in range(len(timpNP)):
    if timpNP[i] <= -15:
        timpNP[i] = -15
        
plt.yscale('log')
plt.xlabel('dimensiune')
plt.ylabel('timp')
plt.plot(dimensiuni, timpPersonal, color='blue')
plt.plot(dimensiuni, timpNP, color='red')
plt.savefig('ex1.pdf', format='pdf')
plt.savefig('ex1.png', format='png')