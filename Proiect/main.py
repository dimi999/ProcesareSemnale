import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image

img = np.array(Image.open('D:/procesareSemnale/Proiect/Tulsa.png').convert('L'))

width, height = img.shape[1], img.shape[0]
#img = cv2.imread("D:/procesareSemnale/Proiect/geometrydash.png", cv2.IMREAD_GRAYSCALE)
plt.imshow(img)
print(img.shape)
plt.figure()

gradient = cv2.Sobel(img, cv2.CV_16U, 1, 0)
#gradient = cv2.Laplacian(img, cv2.CV_16U)
plt.imshow(gradient, cmap='gray')
plt.figure()

threshold = 100

gradient[gradient >= threshold] = 255
gradient[gradient < threshold] = 0
print(np.sum(gradient) / 255)
plt.imshow(gradient, cmap='gray')
plt.figure()
#%%

theta_count = 180

diag_len = int(np.sqrt(width**2 + height**2))
rho_count = 2 * diag_len + 1

Accumulator = np.matrix(np.zeros((theta_count, rho_count)))
theta = np.linspace(0, np.pi, theta_count)
rho = np.linspace(-diag_len, diag_len, rho_count)

#%%

cosines = np.cos(theta) 
sines = np.sin(theta)

arr = dict()

ct = 0
for i in range(gradient.shape[0]):
    for j in range(gradient.shape[1]):
        if gradient[i][j] == 255: 
            x, y = j, gradient.shape[0] - i - 1
            ct += 1
            
            if ct % 100 == 0:
                print(ct)
            for th in range(theta_count):
                ro = int(round(x * cosines[th] + y * sines[th]))
                Accumulator[th, ro + diag_len] += 1
#%%
plt.imshow(Accumulator * 10)
plt.figure()
print(Accumulator[:16,:16],Accumulator[Accumulator>=100])
#%%

threshold_vote = 380 

plt.imshow(img)


def get_coord(th, ro):
    if abs(np.sin(th)) < 1e-2:
        return (ro / np.cos(th), 'vertical_line')
    if abs(np.cos(th)) < 1e-2:
        m = 0.
    else:
        m = - 1 / np.tan(th)   
    c = ro / np.sin(th)
    
    return (m, c)
    
def draw_line(m, c):
    if c == 'vertical_line':
        if m < 0:
            return
        samples = [m for i in range(100)]
        values = np.linspace(0, height, 100)
        plt.plot(samples, values, c='red', linewidth=0.5)
        return
    samples = np.linspace(0, width, 100)
    samples = samples[height - (samples * m + c) <= height]
    samples = samples[height - (samples * m + c) >= 0]
    values = height - (m * samples + c)
    if len(samples) > 1:
        plt.plot(samples, values, c='red', linewidth=.5)


for i in range(Accumulator.shape[0]):
    for j in range(Accumulator.shape[1]):
        if Accumulator[i,j] > threshold_vote:
            th, ro = theta[i], rho[j]
            m, c = get_coord(th, ro)
#            print(m, c)
            draw_line(m, c)
        
