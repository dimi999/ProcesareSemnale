import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image


#https://gist.github.com/kylemcdonald/bedcc053db0e7843ef95c531957cb90f
def full_frame(width=None, height=None):
    import matplotlib as mpl
    mpl.rcParams['savefig.pad_inches'] = 0
    figsize = None if width is None else (width, height)
    fig = plt.figure(figsize=figsize)
    ax = plt.axes([0,0,1,1], frameon=False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.autoscale(tight=True)
    
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
        values = np.linspace(1, height - 1, 100)
        plt.plot(samples, values, c='black', linewidth=.5)
        return
    samples = np.linspace(0, width, 100)
    samples = samples[height - (samples * m + c) <= height]
    samples = samples[height - (samples * m + c) >= 0]
    values = height - (m * samples + c)
    if len(samples) > 1:
        plt.plot(samples, values, c='black', linewidth=.5)
        
def score_compute(img1, img2):
    correct, incorrect, missing = 0, 0, 0
    global img5
    for i in range(height):
        for j in range(width):
            if img1[i,j] != img2[i,j]:
                img5[i,j] = abs(img1[i,j] - img2[i,j])
                if img5[i,j] <= 20 and img2[i,j] <= 50: 
                    #acceptable differnece between blacks
                    correct += 1
                elif img1[i, j] <= 30: # wrong line
                    incorrect += 1
                elif img2[i,j] <= 30: # missing line
                    missing += 1 
    if correct == 0 and (incorrect == 0 or missing ==0):
        return 0 #image is empty
    
    return correct / (missing * incorrect)

    

imgs = ['test_stea.png']#['test_linii.png', 'test_sah.png', 'test_triunghi.png', 'test_concav.png', 'test_stea.png']
correct_imgs = ['test_stea_corect.png']#['test_linii_corect.png', 'test_sah_corect.png', 'test_triunghi_corect.png', 'test_concav_corect.png', 'test_stea_corect.png']

gradient_threshold = [85] #[65,70,85,110,125]
voting_threshold = [70]#[40,55,70,85]

max_score = 0
optimal_thresholds = []

for it_gradient in range(len(gradient_threshold)):
    for it_vot in range(len(voting_threshold)):
        score = 0
        for it in range(len(imgs)):
        
            #Spyder is funny and needs the whole path for some reason
            img = np.array(Image.open(f'D:/procesareSemnale/Proiect/{imgs[it]}'))
            img = cv2.cvtColor(img[:,:,:3], cv2.COLOR_RGB2GRAY)
            width, height = img.shape[1], img.shape[0]
            plt.imshow(img)
            plt.figure()
            
            #gradient = cv2.Sobel(img, cv2.CV_16U, 1, 0)
            gradient = cv2.Laplacian(img, cv2.CV_16U)
            plt.imshow(gradient, cmap='gray')
            plt.figure()
            
            threshold = gradient_threshold[it_gradient]
            
            gradient[gradient >= threshold] = 255
            gradient[gradient < threshold] = 0
            plt.imshow(gradient, cmap='gray')
            plt.figure()

        
            theta_count = 180
            
            diag_len = int(np.sqrt(width**2 + height**2))
            rho_count = 2 * diag_len + 1
            
            Accumulator = np.matrix(np.zeros((theta_count, rho_count)))
            theta = np.linspace(0, np.pi, theta_count)
            rho = np.linspace(-diag_len, diag_len, rho_count)
            

            
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
#This cell is useful for plotting the accumulator, and seeing data
#For instance how many cells are above a threshold
#ax = plt.gca()
#plt.xlabel('Theta', fontsize=18)
#plt.ylabel('Rho', fontsize=18)
#ax.get_xaxis().set_ticks([])
#ax.get_yaxis().set_ticks([])
#plt.imshow(Accumulator.T, cmap='hot', aspect='auto')
#plt.savefig('D:/procesareSemnale/Proiect/tabel_rho_theta.png', format='png')
#plt.show()
#plt.figure()
#print(Accumulator[Accumulator>=100])
            #%%
            threshold_vote = voting_threshold[it_vot] 
        
            full_frame()
            plt.imshow(img, cmap='gray', alpha=1)
            
            for i in range(Accumulator.shape[0]):
                for j in range(Accumulator.shape[1]):
                    if Accumulator[i,j] > threshold_vote:
                        th, ro = theta[i], rho[j]
                        m, c = get_coord(th, ro)
                        draw_line(m, c)
            
            
            plt.savefig(f'D:/procesareSemnale/Proiect/{imgs[it][:-4]}_Hough.png', format='png')
            plt.show()
            plt.figure()
            #%%
            img2 = np.array(Image.open(f'D:/procesareSemnale/Proiect/{imgs[it][:-4]}_Hough.png'))
            img2 = cv2.cvtColor(img2[:,:,:3], cv2.COLOR_RGB2GRAY)
            #%%
            plt.imshow(img2, cmap='gray')
            plt.show()
            img3 = np.array(Image.open(f'D:/procesareSemnale/Proiect/{correct_imgs[it]}'))
            img3 = cv2.cvtColor(img3[:,:,:3], cv2.COLOR_RGB2GRAY)
            #plt.imshow(img3, cmap='gray')
            #plt.show()  
            
            img5 = np.zeros((height, width))
            
            score += (score_compute(img2, img3)) / len(imgs)
            
            #plt.imshow(img5)
            #plt.show()
        if score > max_score:
            optimal_thresholds = [gradient_threshold[it_gradient], voting_threshold[it_vot]]
            max_score = score
            
print(optimal_thresholds, max_score)
        
