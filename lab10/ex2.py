import matplotlib.pyplot as plt
import numpy as np

def liniar(x, y):
    return x * y

def brownian(x, y):
    return min(x, y)

def quadratic_exp(x, y, alfa=100):
    return np.exp(-alfa * np.linalg.norm(x - y) ** 2)

def Ornstein_Uhlenbeck(x, y, alfa=5):
    return np.exp(-alfa * np.abs(x - y))

def plot_process(kernel):
    space = np.linspace(-1, 1, 500)
    covar = np.array([[kernel(x, y) for x in space] for y in space])
    samples = np.random.multivariate_normal(np.zeros(500), covar)
    plt.plot(space, samples)
    

for i in range(10):
    plot_process(liniar)

plt.figure()
plt.savefig('ex2liniar.pdf', format='pdf')
plt.savefig('ex2liniar.png', format='png')

plot_process(brownian)
plt.figure()
plt.savefig('ex2brownian.pdf', format='pdf')
plt.savefig('ex2brownian.png', format='png')

plot_process(quadratic_exp)
plt.figure()
plt.savefig('ex2quadratic_exp.pdf', format='pdf')
plt.savefig('ex2quadratic_exp.png', format='png')

plot_process(Ornstein_Uhlenbeck)
plt.figure()
plt.savefig('ex2Ornstein_Uhlenbeck.pdf', format='pdf')
plt.savefig('ex2Ornstein_Uhlenbeck.png', format='png')
