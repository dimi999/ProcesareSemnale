import numpy as np
import matplotlib.pyplot as plt

x = np.genfromtxt('D:/procesareSemnale/Lab5/Train.csv', delimiter=',')

vals = x[:,2]
vals = vals[1:]

#%% Ex a 
#Frecventa de esantionare 1 sample / h => 1 / 3600 Hz

#%% Ex b
#Ora de final 25.09.2014 ora 23
#Ora de inceput 25.08.2012 ora 00
#Intervalul e de un an o luna si 23 de ore

#%% Ex c
#Fv maxim = Fv Esantionare / 2 = 1 / 7200 Hz

#%% Ex d

N = vals.shape[0]

fftVals = np.fft.fft(vals)
fftVals = abs(fftVals / N)
fftVals = fftVals[:N // 2]
freqs = (1 / 3600) * np.linspace(0, N / 2, N // 2) / N
plt.stem(freqs, fftVals)
plt.xlabel('Frecventa')
plt.ylabel('Valoarea')

plt.savefig('Punctuld.png', format='png')
plt.savefig('Punctuld.pdf', format='pdf')

#%% Ex e
# Da are, deoarece valoarea in 0 este diferita de 0

print(fftVals[0])
avgVals = np.average(vals)
vals = vals - avgVals

fftVals = np.fft.fft(vals)
fftVals = abs(fftVals / N)
fftVals = fftVals[:N // 2]
freqs = (1 / 3600) * np.linspace(0, N / 2, N // 2) / N
plt.stem(freqs, fftVals)
plt.xlabel('Frecventa')
plt.ylabel('Valoarea')
print(fftVals[0])

plt.savefig('Punctule.png', format='png')
plt.savefig('Punctule.pdf', format='pdf')

#%% Ex f
big5 = fftVals.argsort()[-5:][::-1]
print(fftVals[big5])
print(freqs[big5] * 3600 * 24 * 365)

#Sunt periodicitatile intregii perioade, zilei, anului si una care corespunde aproximativ unei perioade de 8 luni, dar a cincea este pentru saptamna

#%% Ex g

values = []
startEsantion = 1056
for i in range(startEsantion, startEsantion + 720):
    values.append(vals[i])
values = np.array(values)
samples = np.linspace(0, 720, 720)

plt.plot(samples, values)
plt.xlabel('Timpul (h)')
plt.ylabel('Valoarea')

plt.savefig('Punctulg.png', format='png')
plt.savefig('Punctulg.pdf', format='pdf')

#%%Ex h

#Putem corela graficul cu alte date posibil cunoscute cum ar fi,
     #numarul de masini inmatriculate in zona
     #cresterea populatiei din zona
     #cresterea afacerilor din zona
     
     #Cons: -avem nevoie de un numar mare de date
     #      -trebuie sa analizam corelatia dintre multe evenimente
     
#Putem analiza cresterea constanta care se vede si analiza valoarea din prezent
    #Cons: -Presupunem o crestere constanta a valorii
    #      -Avem nevoie de un timp mai lung de masurare a prezentului pentru a evita eventuale spikeuri

#%% Ex i

freqElim = 0.00004630136 #Frecventa aferenta unui sfert de zi, aproximativ
fftVals = np.fft.fft(vals)
for i in range(len(freqs)):
    if freqs[i] > freqElim:
        fftVals[i : len(fftVals) - i] = 0
        break

signalSmoothed = np.fft.ifft(fftVals)

fig, axs = plt.subplots(2)
fig.suptitle('Punctul i pe un subinterval')

for ax in axs.flat:
    ax.set_xlabel('Timp (h)')
    ax.set_ylabel('Valoare')

axs[0].plot(signalSmoothed.real[2000:2500])
axs[1].plot(vals[2000:2500], color='red')

plt.savefig('Punctuli.png', format='png')
plt.savefig('Punctuli.pdf', format='pdf')

