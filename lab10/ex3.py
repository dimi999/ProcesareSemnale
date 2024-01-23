import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("co2_daily_mlo.csv", header=None)
#df.columns = ["YYYY", "MM", "DD", "Frac_Date", "CO2"]

print(df.values[0])

last = df.values[0][1]
avg = df.values[0][4]
avgs = []
ct = 1

for i in range(1, len(df.values)):
    if df.values[i][1] != last:
        avgs.append(avg / ct)
        last = df.values[i][1]
        avg = 0
        ct = 0
    avg += df.values[i][4]
    ct += 1
avgs = np.array(avgs)
plt.plot(avgs)

#Sitem de ecuatii cu 2 necunoscute m * idx + t * 1 = av, m = x1, t = x2 
A = np.matrix(np.zeros((len(avgs), 2)))
b = avgs

for i in range(len(avgs)):
    A[i,0] = i
    A[i, 1] = 1

sol = np.linalg.lstsq(A, b, rcond=None)
m, t = sol[0][0], sol[0][1]

samples = np.linspace(0, len(avgs), len(avgs))
plt.plot(samples * m + t)
plt.savefig('ex3a.pdf', format='pdf')
plt.savefig('ex3a.png', format='png')

#%%
series = avgs - (samples * m + t)
plt.figure()

plt.plot(series)
plt.savefig('ex3b.pdf', format='pdf')
plt.savefig('ex3b.png', format='png')

#Putem deduce din grafic ca pare destul de periodic semnalul asa ca vom folosi kernelul periodic

#%%
def periodic_kernel(x, y, alfa=1, beta=1):
    return np.exp(-alfa * np.sin(beta * np.pi * (x - y)) ** 2)

start = len(series) - 12
predict_series = series[:-12]
samples = np.linspace(start, start + 12, 12)


mean = np.array([np.mean(series) for i in range(len(predict_series) + 12)])
covar = np.zeros((len(predict_series) + 12, len(predict_series) + 12))

for i in range(12):
    for j in range(12):
        covar[i,j] = periodic_kernel(samples[i], samples[j])

for i in range(12, 12 + len(predict_series)):
    for j in range(12):
        covar[i,j] = periodic_kernel(predict_series[i - 12], samples[j])

for i in range(12):
    for j in range(12, 12 + len(predict_series)):
        covar[i,j] = periodic_kernel(samples[i], predict_series[j - 12])

for i in range(12, 12 + len(predict_series)):
    for j in range(12, 12 + len(predict_series)):
        covar[i,j] = periodic_kernel(predict_series[i - 12], predict_series[j - 12])

print(covar.shape, mean.shape)

samples_regression = np.random.multivariate_normal(mean, covar)
plt.plot(samples_regression * m + t)


    


