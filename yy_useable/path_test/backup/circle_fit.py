from scipy import optimize as opt
import numpy as np

def circle(data, xc, yc):
    return np.sqrt((data[:, 0]-xc)**2 + (data[:, 1]-yc)**2)

def cost_fun(c, data):
    Ri = circle(data, *c)
    return np.square(Ri - Ri.mean())

def circle_lsq(data):
    center_ = np.mean(data, axis = 0)
    center, _ = opt.leastsq(cost_fun, (center_[0], center_[1]), args=(data, ))
    R = np.mean(circle(data, center[0], center[1]))
    return center[0], center[1], R