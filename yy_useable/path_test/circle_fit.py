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

def cost_tz(x, cnt, pix):
    x_ = cnt[:, 0] * (pix[:, 2] + x[0]) - pix[:, 0]
    y_ = cnt[:, 1] * (pix[:, 2] + x[0]) - pix[:, 1]
    return np.sum(np.sqrt(x_ * x_ + y_ * y_))

def prime_tz(x, cnt, pix):
    x_ = cnt[:, 0] * (pix[:, 2] + x[0]) - pix[:, 0]
    y_ = cnt[:, 1] * (pix[:, 2] + x[0]) - pix[:, 1]
    dz = np.sum((cnt[:, 0] * x_ + cnt[:, 1] * y_) / np.sqrt(x_ * x_ + y_ * y_))
    return np.float32([dz])

def calc_tz(cnt, pix):
    x0 = np.zeros([1], np.float32)
    ret = opt.minimize(cost_tz, x0, (cnt, pix), jac = prime_tz)
    return ret.x

def cost_t(x, cnt, pix):
    x_ = cnt[:, 0] * (pix[:, 2] + x[2]) - pix[:, 0] - x[0]
    y_ = cnt[:, 1] * (pix[:, 2] + x[2]) - pix[:, 1] - x[1]
    return np.sum(np.sqrt(x_ * x_ + y_ * y_))

def prime_t(x, cnt, pix):
    x_ = cnt[:, 0] * (pix[:, 2] + x[2]) - pix[:, 0] - x[0]
    y_ = cnt[:, 1] * (pix[:, 2] + x[2]) - pix[:, 1] - x[1]
    tp = np.sqrt(x_ * x_ + y_ * y_)
    dx = -np.sum(x_ / tp)
    dy = -np.sum(y_ / tp)
    dz = np.sum((cnt[:, 0] * x_ + cnt[:, 1] * y_) / tp)
    return np.hstack([dx, dy, dz])

def calc_t(cnt, pix): 
    x0 = np.zeros([3], np.float32)
    ret = opt.minimize(cost_t, x0, (cnt, pix), jac = prime_t)
    return ret.x