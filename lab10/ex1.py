import matplotlib.pyplot as plt
import numpy as np

def gaussian_1d(avg, var):
    x = np.random.normal()
    return avg + x * np.sqrt(var)

samples =[gaussian_1d(2, 2) for i in range(1000)]
        
plt.hist(samples, bins=100)

print(np.mean(samples), np.var(samples))

# Asta e pt verificare vizuala
samples2 = np.random.normal(2, 2, size=1000)
plt.figure()
print(np.max(samples))

plt.hist(samples2, bins=100)

#%%

def gaussian_2d(avg, var):
    vals, vecs = np.linalg.eig(var)
    lamb = [[np.sqrt(vals[0]), 0], [0, np.sqrt(vals[1])]]
    x = np.random.multivariate_normal([0, 0], [[1, 0], [0, 1]])
    lamb = np.array(lamb)
    x = np.array(x)
    avg = np.array(avg)
    
    return vecs @ lamb @ x + avg

def pdf_2d(x, avg, sigma):
    return 1 / (np.pi * 2 * np.sqrt(np.linalg.det(sigma))) * \
            np.exp(-1/2 * (x - avg).T * np.linalg.inv(sigma) * (x - avg)) 
    
var = [[1, 3/5], [3/5, 2]]
avg = [0, 0]
samples = np.array([gaussian_2d(avg, var) for i in range(1000)])
plt.scatter(samples[:,0], samples[:,1])
z = [pdf_2d(sample, np.array(avg), np.array(var)) for sample in samples]
z = np.array(z)
plt.scatter(z[:,0], z[:,1], c='red')

