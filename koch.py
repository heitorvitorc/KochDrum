# import libraries
import numpy as np
import matplotlib.pyplot as plt

# ignore warnings
import warnings
warnings.filterwarnings("ignore")

def rotate(p, origin=(0, 0), angle=0):
    """
    Angle in radians
    """
    # angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    o = np.atleast_2d(origin)
    p = np.atleast_2d(p)
    return np.squeeze((R @ (p.T-o.T) + o.T).T)


def add_segment(start, end):
    """
    Segments a line to Koch line, creating fractals.
  
    """
   
    # the length of the segment
    L = np.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    dx = end[0]-start[0]; dy = end[1]-start[1]
    
    # Find angle between given line and reference line

    if np.isclose(dx, 0.): #! ERROR FIX
        dx = 0
        slope = 1 # It is actually infinity
        if dy > 0:
            theta = np.pi/2
        else:
            theta = - np.pi/2
    elif np.isclose(dy, 0.):
        dy = 0
        if dx > 0:
            slope = 0 # It is a horizontal line
            theta = 0
        else:
            theta = np.pi
    elif dx != 0 and dy != 0:
        slope = dy/dx
        theta = np.arctan(slope)


    # rotate end point to obtain reference coordinates
    refend = rotate(end,start,-theta)

    # coordinates of the start
    x1, y1 = start[0], start[1]
    
    # coordinates of the end
    x2, y2 = refend[0], refend[1]

    a = (x1, y1); b = (x1 + L/4.), y1   
    c = b[0], (b[1] + L/4.); d = (c[0] + L/4), c[1]
    e = d[0], (d[1] - L/4.); f = e[0], (e[1] -L/4.)
    g = (f[0] + L/4.), f[1]; h = g[0], (g[1] + L/4.)
    i = x2,y2

    points = [a, b, c, d, e, f, g, h, i]

    # rotate additional segments to original reference
    points = rotate(points,origin=start,angle=theta)

    return points[1:-1]

def koch_fractal(points, level):

    newpts = []
    for i in range(1,len(points)):
        start = points[i-1]; end = points[i]
        new = add_segment(start, end)
        newpts.append(start)
        for item in new:
            newpts.append(item.tolist())
    newpts.append(end)

    if level == 0:
        return newpts
    else:
        return koch_fractal(newpts, level-1)
    

A = [0., 0.]
B = [1., 0.]
C = [1., 1.,]
D = [0., 1.]
pts0 = [A, B, C, D, A]

level = 6
points_rec = koch_fractal(pts0, level)

pts0 = np.asarray(pts0)
points = np.asarray(points_rec)

plt.plot(pts0[:,0],pts0[:,1], label = 'level 0'); plt.legend()
plt.plot(points[:,0],points[:,1], label = 'level '+ str(level)); plt.legend()

plt.show()
k = 1