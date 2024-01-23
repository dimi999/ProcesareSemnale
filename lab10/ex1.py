import matplotlib.pyplot as plt
import numpy as np

def gaussian_1d(avg, var):
    x = np.random.normal()
    return avg + x * np.sqrt(var)

samples =[gaussian_1d(2, 2) for i in range(1000)]
        
plt.hist(samples, bins=100)

plt.savefig('ex11d.pdf', format='pdf')
plt.savefig('ex11d.png', format='png')

# Asta e pt verificare vizuala
samples2 = np.random.normal(2, 2, size=1000)
plt.figure()

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
            np.exp(-1/2 * ((x - avg) @ np.linalg.inv(sigma) @ (x - avg))) #Nu avem nevoie de transpusa datorita felului in care numpy inmulteste vectorii
    
var = [[1, 3/5], [3/5, 2]]
avg = [0, 0]
samples = np.array([gaussian_2d(avg, var) for i in range(5000)])
plt.figure()
ax = plt.gca()
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
plt.scatter(samples[:,0], samples[:,1])

x = np.linspace(-5, 5, 500)
y = np.linspace(-5, 5, 500)

z = np.zeros((500, 500))
for i in range(500):
    for j in range(500):
        z[i,j] = pdf_2d(np.array([x[i], y[j]]), np.array(avg), np.array([[2, 3/5], [3/5, 1]])) #Nu inteleg dc trebuie inversata aici diagonala principala
plt.contour(x, y, z)
plt.savefig('ex12d.pdf', format='pdf')
plt.savefig('ex12d.png', format='png')
