import matplotlib.pyplot as plt
import numpy as np

width = 256
height = 256
mat = np.zeros((width, height))

for i in range(height):
    for j in range(width):
        if (i // 32 + j // 32) % 2 == 0:
            mat[i, j] = 1
        else:
            mat[i, j] = np.random.random() * 0.6

print(mat[:8, :8])
plt.axis('off')
plt.imshow(mat, cmap='gray')
plt.savefig('D:/procesareSemnale/Proiect/test_sah.png', format='png')
plt.show()

width = 256
height = 256
mat = np.ones((width, height))

for i in range(height):
    for j in range(width):
        if i % 32 == 0 or j % 32 == 0:
            mat[i,j] = 0
plt.axis('off')
plt.imshow(mat, cmap='gray')
plt.savefig('D:/procesareSemnale/Proiect/test_sah_corect.png', format='png')
plt.show()

#%%
def draw_lines(ax, lines):
    for line in lines:
        if line[0] == "vertical":
            samples = np.linspace(1, width - 1, 150)
            values = [line[1]] * 150
        else:
            samples = np.linspace(1, width - 1, 150)
            values = line[0] * samples + line[1]
        ax.plot(samples, values, c='red', linewidth=.5)
        
def compute_lines(points):
    last = points[0]
    lines = []
    for i in range(1, len(points)):
        crt = points[i]
        if crt[0] == last[0]:
            m = 'vertical'
            c = crt[0]
        else:
            m = (crt[1] - last[1]) / (crt[0] - last[0])
            c = crt[1] - crt[0] * m
        lines.append([m, c])
        last = crt
    if len(points) >= 3:
        crt = points[0]
        if crt[0] == last[0]:
            m = 'vertical'
            c = crt[0]
        else:
            m = (crt[1] - last[1]) / (crt[0] - last[0])
            c = crt[1] - crt[0] * m
        lines.append([m, c])
    return lines

def full_frame(width=None, height=None):
    import matplotlib as mpl
    mpl.rcParams['savefig.pad_inches'] = 0
    figsize = None if width is None else (width, height)
    fig = plt.figure(figsize=figsize)
    ax = plt.axes([0,0,1,1], frameon=False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.autoscale(tight=True)
    
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
# Coordinates of our triangle
full_frame()
pts = np.array([[3,18], [2,2], [15,8]])
p = Polygon(pts, color="black")
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(1,20)
ax.set_ylim(1,20)
plt.axis('off')
plt.savefig('D:/procesareSemnale/Proiect/test_triunghi.png', format='png')
plt.show()

full_frame()
p = Polygon(pts, color="black")
ax = plt.gca()
#ax.add_patch(p)
ax.set_xlim(1,20)
ax.set_ylim(1,20)
draw_lines(ax, compute_lines(pts))
plt.axis('off')
plt.savefig('D:/procesareSemnale/Proiect/test_triunghi_corect.png', format='png')
plt.show()


#%%
line1 = plt.Line2D((2, 4), (5, 6), lw=2, alpha = 0.7, color='black')
line2 = plt.Line2D((2, 8), (4, 4), lw=2, alpha = 0.9, color='black')
line3 = plt.Line2D((8, 5), (9, 2), lw=2, alpha = 0.2, color='black')
line4 = plt.Line2D((6, 3), (3, 6), lw=2, alpha = 0.4, color='black')
line5 = plt.Line2D((7, 9), (7, 1), lw=2, alpha = 0.6, color='black')
ax = plt.gca()
# Adding a line to the plot:
ax.add_line(line1)
ax.add_line(line2)
ax.add_line(line3)
ax.add_line(line4)
ax.add_line(line5)
ax.set_xlim(1,10)
ax.set_ylim(10,1)
plt.axis('off')
plt.savefig('D:/procesareSemnale/Proiect/test_linii.png', format='png')
plt.show()

full_frame()
#p = Polygon(pts, color="black")
ax = plt.gca()
#ax.add_patch(p)
ax.set_xlim(1,10)
ax.set_ylim(10,1)

draw_lines(ax, compute_lines([(2, 5), (5, 6)]))
draw_lines(ax, compute_lines([(2, 4), (1, 4)]))
draw_lines(ax, compute_lines([(8, 9), (5, 2)]))
draw_lines(ax, compute_lines([(6, 3), (3, 6)]))
draw_lines(ax, compute_lines([(7, 7), (9, 1)]))
plt.axis('off')
plt.savefig('D:/procesareSemnale/Proiect/test_linii_corect.png', format='png')
plt.show()
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
# Coordinates of our polygon
pts = np.array([[30,60], [75,70], [100,55], [130,55], [115, 20], [55,34]])
p = Polygon(pts, color="black")
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(20,150)
ax.set_ylim(15,90)
plt.axis('off')
plt.savefig('D:/procesareSemnale/Proiect/test_concav.png', format='png')
plt.show()

p = Polygon(pts, color="black", alpha=0)
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(20,150)
ax.set_ylim(15,90)
draw_lines(ax, compute_lines(pts))
plt.axis('off')
plt.savefig('D:/procesareSemnale/Proiect/test_concav_corect.png', format='png')
plt.show()
#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
# Coordinates of our star
pts = np.array([[50,60], [45,40], [30,40], [42,30], [40, 10],\
                [50,25],[60,10],[58,30],[70,40],[55,40]])
p = Polygon(pts, color="black")
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(20,85)
ax.set_ylim(5,70)
plt.axis('off')
plt.savefig('D:/procesareSemnale/Proiect/test_stea.png', format='png')
plt.show()

p = Polygon(pts, color="black")
ax = plt.gca()
ax.add_patch(p)
ax.set_xlim(20,85)
ax.set_ylim(5,70)
draw_lines(ax, compute_lines(pts))
plt.axis('off')
plt.savefig('D:/procesareSemnale/Proiect/test_stea_corect.png', format='png')
plt.show()
    
    



