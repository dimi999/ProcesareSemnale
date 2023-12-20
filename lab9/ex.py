#%%ex1, 2
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



alfa = 0.69
data = values[:800]

predictions = [data[799]]

for i in range(1, 200):
    predictions.append(alfa * values[i + 799] + predictions[i - 1] * (1 - alfa))

predictions = np.array(predictions)
error = np.mean((predictions - values[800: 1000])**2)
print(error)

fig, axs = plt.subplots(3)
fig.suptitle('Exercitiul 2')
axs[0].plot(values[801:], color='red')
axs[0].plot(predictions, color='green')
l1, = axs[1].plot(values[801:], color='red')
l2, = axs[2].plot(predictions, color='green')
plt.legend([l1, l2], ['Predicted', 'Actual'])

plt.savefig("ex1.pdf", format="pdf")
plt.savefig("ex1.jpg", format="jpg")

val = 0
errors = []

for alfa in range(1, 10000):
    alfa = alfa / 10000
    predictions_new = [data[799]]
    for i in range(1, 200):
        predictions_new.append(alfa * values[i + 799] + predictions[i - 1] * (1 - alfa))

    predictions = np.array(predictions)
    error = np.mean((predictions_new - values[800: 1000])**2)
    errors.append(error)

plt.figure()   
plt.plot(np.array(errors))

plt.savefig("ex1eroare.pdf", format="pdf")
plt.savefig("ex1eroare.jpg", format="jpg")

#%% ex 3

q = 25
m = 100
noise = []

for i in range(m + q):
    noise.append(np.random.normal())

mean = np.sum(data) / 800

sample = np.zeros(m)

for i in range(m):
    sample[i] = data[800 - m + i] - noise[q + i] - mean

Y = np.zeros((m, q))

for i in range(m):
    Y[i] = noise[i : i + q]

teta = np.linalg.lstsq(Y, sample, rcond=None)[0]

print(teta)

#%% Ex 4

from statsmodels.tsa.arima.model import ARIMA

errors = []
min_error = 1e5
p_min, q_min = 0, 0


ARMA = ARIMA(data[:800],
             order=([p for p in range(1, 21)], 0, [q for q in range(1, 21)]),
             trend = 'ct')

ARMA = ARMA.fit()
predictions = ARMA.forecast(200)
error = np.mean((predictions - values[800: 1000])**2)
        
print(error)

