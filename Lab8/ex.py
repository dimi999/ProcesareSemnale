import numpy as np
import scipy
import matplotlib.pyplot as plt

def trendSignal(sample):
    return 0.5 * sample**2 + 2 * sample + 7

def seasonSignal(sample):
    return np.sin(25 * 2 * np.pi * sample) + np.sin(15 * 2 * np.pi * sample)

white_noise = np.random.normal(0, 1, 1000)

samples = np.linspace(0, 5, 1000)

values = trendSignal(samples) + seasonSignal(samples) + white_noise

fig, axs = plt.subplots(4)
fig.suptitle('Exercitiul 1a')
axs[0].plot(values)
axs[1].plot(trendSignal(samples))
axs[2].plot(seasonSignal(samples))
axs[3].plot(white_noise)

plt.savefig('1a.jpg', format='jpg')
plt.savefig('1a.pdf', format='pdf')

#%% ex b
autoCorr = np.correlate(values, values, mode='full')
autoCorr = autoCorr[autoCorr.size // 2:]
plt.figure()
plt.plot(autoCorr)

plt.savefig('1b.jpg', format='jpg')
plt.savefig('1b.pdf', format='pdf')

#%% ex c

p = 10
m = 200
def AR(p, m):
    Y = np.matrix(np.zeros((m - p, p)))
    
    for i in range(m - p):
        for j in range(p):
            Y[i,j] = values[m - i - j - 1]
    
    y_mic = values[p + 1 : m + 1]
    
    #Trebuie sa rezolvam sistemul Y * x = y_mic
    x = np.linalg.lstsq(Y, y_mic)[0]
    
    predictions = []
    
    for i in range(m + 1, 1000):
        y_crt = np.array([[values[i - 1 - t]] for t in range(p)])
        
        predictions.append(np.dot(y_crt.T, x))
    
    predictions = np.array(predictions)
    error = np.mean((predictions - values[m + 1: 1000])**2)
    #print(error)
    return (error, predictions)

error, predictions = AR(p, m)
fig, axs = plt.subplots(3)
axs[0].plot(predictions, color='red')
axs[0].plot(values[m + 1: 1000], color='blue')
l1, = axs[1].plot(predictions, color='red')
l2, = axs[2].plot(values[m + 1: 1000], color='blue')
plt.legend([l1, l2], ['Predicted', 'Actual'])
plt.savefig('1c.jpg', format='jpg')
plt.savefig('1c.pdf', format='pdf')

#%% ex d

minError = 1e9
popt, mopt = 0, 0

for p in range(2, 25):
    for m in range(p + 1, 300):
        error, _ = AR(p, m)
        if error < minError:
            minError, popt, mopt = error, p, m
            
print(minError, popt, mopt)
        