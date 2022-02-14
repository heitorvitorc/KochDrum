import numpy as np
import matplotlib.pyplot as plt
# from shapely.geometry import Point

from koch import *

# Create initial square to grow the koch fractal
A = [0., 0.]
B = [1., 0.]
C = [1., 1.,]
D = [0., 1.]
pts0 = [A, B, C, D, A]

level = 0 # Level of the fractal structure
points = generate_koch(pts0, level)

# Define lattice constante delta
delta = np.abs(points[0,0]-points[1,0])

# Get width and height of fractal
xmin = np.min(points[:,0]); xmax = np.max(points[:,0])
ymin = np.min(points[:,1]); ymax = np.max(points[:,1])

box = np.asarray([(xmin,ymin), (xmax,ymin), (xmax,ymax), (xmin,ymax), (xmin,ymin)])

# Create meshgrid 
nx = np.linspace(xmin, xmax, delta)
ny = np.linspace(ymin, ymax, delta)
X, Y = np.meshgrid(nx,ny)

fig = plt.figure(); ax = fig.add_subplot(111)
ax.plot(box[:,0],box[:,1], color='black',linestyle='dashed'); plt.legend()
ax.plot(points[:,0],points[:,1], label = 'level '+ str(level)); plt.legend()
ax.set_aspect("equal", "box")
plt.show()