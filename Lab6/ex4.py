import matplotlib.pyplot as plt
import numpy as np
import scipy

#%% Ex4a

x = np.genfromtxt('D:/procesareSemnale/Lab6/Train.csv', delimiter=',')

vals = x[:,2]
vals = vals[1 : 73]
print(len(vals))

#%% Ex4b

avgs = [5, 9, 13, 17]
fig, axs = plt.subplots(4)
for w in range(4):
    avg = np.convolve(vals, np.ones(avgs[w]), 'valid') / avgs[w]
    print(avg)
    axs[w].plot(np.linspace(0, len(avg) - 1, len(avg)), avg)
    print(len(avg))
    
for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')

plt.savefig('ex4b.png', format='png')
plt.savefig('ex4b.pdf', format='pdf')

#%% Ex4c
#Frecventa de esantionare e de 1/3600 Hz => 
#Putem reconstrui doar semnale de frecventa 1/7200Hz sau mai mici =>
#Consideram frecventa mare ceea ce se intampla la 4h 1/14400 Hz =>
#Frecventa normalizata este 1/2

#%% Ex4d

butterB, butterA = scipy.signal.butter(5, 0.5)
chebyB, chebyA = scipy.signal.cheby1(5, 5, 0.5)

w,h = scipy.signal.freqz(butterB, butterA)
plt.plot(w, 20 * np.log10(abs(h)))
w,h = scipy.signal.freqz(chebyB, chebyA)
plt.plot(w, 20 * np.log10(abs(h)), color='red')

for ax in axs.flat:
    ax.set_xlabel('Frecventa')
    ax.set_ylabel('Valoare')

plt.savefig('ex4d.png', format='png')
plt.savefig('ex4d.pdf', format='pdf')



#%% Ex4e
samples = np.linspace(0, len(vals) - 1, len(vals))
filterdButter = scipy.signal.filtfilt(butterB, butterA, vals)
filterdCheby = scipy.signal.filtfilt(chebyB, chebyA, vals)


fig, axs = plt.subplots(2)
axs[0].plot(samples, vals)
axs[0].plot(samples, filterdButter, color='red')
axs[1].plot(samples, vals)
axs[1].plot(samples, filterdCheby, color='red')

for ax in axs.flat:
    ax.set_xlabel('timp')
    ax.set_ylabel('amplitudine')

plt.savefig('ex4e.png', format='png')
plt.savefig('ex4e.pdf', format='pdf')

#As alege filtrul Butterworth deoarece e mai apropiat de semnalul original

#%% Ex4f

butterFilters = [scipy.signal.butter(1, 0.5),
                 scipy.signal.butter(2, 0.5),
                 scipy.signal.butter(5, 0.5),
                 scipy.signal.butter(10, 0.5),
                 ]
chebyFilters = [scipy.signal.cheby1(1, 5, 0.5),
                 scipy.signal.cheby1(2, 3, 0.5),
                 scipy.signal.cheby1(5, 10, 0.5),
                 scipy.signal.cheby1(10, 2, 0.5),
                 scipy.signal.cheby1(1, 4, 0.5),
                 scipy.signal.cheby1(2, 8, 0.5),
                 scipy.signal.cheby1(5, 2, 0.5),
                 scipy.signal.cheby1(10, 5, 0.5),
                 ]


fig, axs = plt.subplots(4)
ct = 0

for (x, y) in butterFilters:
    w,h = scipy.signal.freqz(x, y)
    axs[ct].plot(w, 20 * np.log10(abs(h)))
    ct += 1

for ax in axs.flat:
    ax.set_xlabel('Frecventa')
    ax.set_ylabel('Valoare')

plt.savefig('ex4fbutter.png', format='png')
plt.savefig('ex4fbutter.pdf', format='pdf')
    
fig, axs = plt.subplots(4)
ct = 0

for (x, y) in chebyFilters[:4]:
    w,h = scipy.signal.freqz(x, y)
    axs[ct].plot(w, 20 * np.log10(abs(h)))
    ct += 1
    
for ax in axs.flat:
    ax.set_xlabel('Frecventa')
    ax.set_ylabel('Valoare')
       
plt.savefig('ex4fcheby.png', format='png')
plt.savefig('ex4fcheby.pdf', format='pdf')


fig, axs = plt.subplots(4)
ct = 0

for (x, y) in chebyFilters[4:]:
    w,h = scipy.signal.freqz(x, y)
    axs[ct].plot(w, 20 * np.log10(abs(h)))
    ct += 1