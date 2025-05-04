import numpy as np
import cv2
def rodrigues(vec, theta):
    vec = np.float32(vec).reshape(3, 1)
    K = np.float32(
        [
            [0, -vec[2, 0], vec[1, 0]],
            [vec[2, 0], 0, -vec[0, 0]],
            [-vec[1, 0], vec[0, 0], 0]
        ]
    )

    return np.cos(theta)*np.eye(3) + (1 - np.cos(theta))*vec*vec.T + np.sin(theta) * K

def rodrigues_cos(vec, cost): # there is no minus sint in our case
    cost = cost if np.abs(cost) < 1.0 else cost / np.abs(cost)
    vec = np.float32(vec).reshape(3, 1)
    K = np.float32(
        [
            [0, -vec[2, 0], vec[1, 0]],
            [vec[2, 0], 0, -vec[0, 0]],
            [-vec[1, 0], vec[0, 0], 0]
        ]
    )
    
    return cost * np.eye(3) + (1 - cost)*vec*vec.T + np.sqrt(1 - cost*cost) * K

def sloveAx(A): #slove Ax = 0
    A = np.concatenate([A, np.ones([A.shape[0], 1], A.dtype)], axis = 1)
    u,sigma,v = np.linalg.svd(A)
    return v[-1]

def KRt2proj(K, R, t):
    proj = np.zeros((3, 4), np.float32)
    proj[0:3, 0:3] = np.float32(R)
    proj[:, 3] = np.float32(t).T
    return np.dot(np.float32(K), proj)

def projection_w2p(pts, K, R, t): #world 2 pix, cam = R.dot(x) + t
    pts = np.concatenate([pts, np.ones([pts.shape[0], 1], pts.dtype)], axis = 1)
    proj = KRt2proj(K, R, t)
    p3d = proj.dot(pts.T).T
    return p3d[:, 0:2] / p3d[:, 2:]

def projection_w2c(pts, R, t): # world 2 camera, cam = R.dot(x) + t
    pts = np.concatenate([pts, np.ones([pts.shape[0], 1], pts.dtype)], axis = 1)
    proj = KRt2proj(np.eye(3), R, t)
    p3d = proj.dot(pts.T).T
    return p3d

def p2w(K_, R_, t_, pt, z_pix): # pix 2 world, cam = R.dot(x) + t
    p3d = np.concatenate([pt * z_pix, z_pix], axis = 1)
    return R_.dot(K_.dot(p3d.T) + t_.reshape([-1, 1])).T

_get_theta = lambda pt, origin: np.arctan2(pt[:, 1] - origin[1], pt[:, 0] - origin[0])

def angle_vec(vec1, vec2):
    norm = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    cost = np.dot(vec1, vec2) / norm
    vec = np.cross(vec1, vec2)
    vec = vec / np.linalg.norm(vec)
    angle = np.arccos(cost)
    angle_ = angle * 180.0 / np.pi
    if angle_ < 1 or angle_ > 179:
        return np.float32([0, 0, 1]), 0.0
    return vec, angle

from circle_fit import circle_lsq
def calc_circle(pt3d): # fit circle
    vec1 = np.float32([1, 0, 0])
    
    #ABD = sloveAx(pt3d[:, 0:2])
    #vec2 = np.float32([ABD[0], ABD[1], 0.0])
    ABCD = sloveAx(pt3d)
    vec2 = ABCD[0:3]
    
    vec, yaw = angle_vec(vec1, vec2)
    
    rot = rodrigues(-vec, yaw)
    pt = rot.dot(pt3d.T).T
    x = np.mean(pt[:, 0])
    y, z, r = circle_lsq(pt[:, 1:3])
    origin = rodrigues(vec, yaw).dot(np.float32([[x], [y], [z]])).T
    #origin = np.mean(pt3d, axis = 0)
    #print(vec2 / np.linalg.norm(vec2), R.dot(vec1))
    theta = _get_theta(pt[:, 1:3], [y, z])
    return origin.reshape([1, -1]), vec, yaw, theta, r

def w2p_sim(KRt, pts):
    pts = np.concatenate([pts, np.ones([pts.shape[0], 1], pts.dtype)], axis = 1)
    p3d = KRt.dot(pts.T).T
    return p3d[:, 0:2] / p3d[:, 2:]

def init_circle(origin, radius, vec, yaw, theta):
    circle = np.zeros([theta.shape[0], 3], np.float32)
    circle[:, 1] = radius * np.cos(theta)
    circle[:, 2] = radius * np.sin(theta)
    rot = rodrigues(vec, yaw)
    return rot.dot(circle.T).T + np.float32(origin).reshape(1, 3), rot.dot(np.float32([[1], [0], [0]]))

def calc_wps(sfm, direction, extra_length):
    vec = rodrigues(sfm.vec, sfm.yaw).dot(np.float32([[extra_length], [0], [0]])).T[0]
    print("calc_wps:", direction, extra_length, vec, "---", sfm.vec, sfm.yaw)
    wps = [sfm.origin[0] + idx * vec * direction for idx in range(-2, 3)]
    return wps

class SFM():
    def __init__(self, origin, vec, yaw):
        self.CAM_K = np.float32([[320, 0, 320], [0, 320,  240], [0, 0, 1]])
        self.CAM_T = np.float32([0.26, -0.0475, 0.0])
        self.Rw2c = np.float32([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
        self.CK = self.CAM_K.dot(self.Rw2c)
        self.CK_inv = np.linalg.inv(self.CK)
        self.SIZE = (640, 480)
        
        self.update_sfm(origin, vec, yaw)
        
    def update_sfm(self, origin, vec, yaw):
        self.origin, self.yaw, self.vec = origin, yaw, vec
        self.ABC = rodrigues(vec, yaw).dot(np.float32([[1], [0], [0]]))
        
    def w2c(self, pts, R, t): # R, t. 相机姿态 same as world, cam = R.dot(x + t)
        return R.dot((pts + (t - self.CAM_T).reshape([1, -1])).T).T
    
    def get_ABCD(self, R, t):
        origin_cam = self.w2c(self.origin.reshape([1, -1]), R, t)
        ABC = R.dot(self.ABC)
        return np.concatenate([ABC, -origin_cam.dot(ABC)], axis = 0)
    
    def w2p(self, pts, R, t): #cam = R.dot(x + t)
        cam = self.w2c(pts, R, t)
        pix = self.CK.dot(cam.T).T 
        img  = pix[:, 0:2] / pix[:, 2:]
        return cam, pix, img
    
    def p2w(self, pts, z_pix, R_, t_): #cam = R.dot(x + t)
        p3d = np.concatenate([pts * z_pix, z_pix], axis = 1)
        return R_.dot(self.CK_inv.dot(p3d.T)).T + (t_ + self.CAM_T).reshape([1, -1])
    
    def p2w_v2(self, pts, R_, t_, ABCD): #cam = R.dot(x + t)
        z_pix = np.ones([pts.shape[0], 1], np.float32)
        pix_ = np.concatenate([pts, z_pix], axis = 1)
        cam_ = self.CK_inv.dot(pix_.T)
        z_pix[:, 0] = -ABCD[3, 0] / (ABCD[0:3].T.dot(cam_))
        return R_.dot(cam_ * z_pix.T).T + (t_ + self.CAM_T).reshape([1, -1])

def get_ellp(thresh, scale = 2): 
    #thresh = np.uint8(np.logical_and(image[:, :, 2] < 240, image[:, :, 2] > 220)) * 128
    #thresh = np.uint8(np.logical_and(image[:, :, 2] < 215, image[:, :, 2] > 195)) * 128
    #thresh = np.uint8(np.logical_and(image[:, :, 2] < 240, image[:, :, 2] > 195)) * 128
    #thresh = np.uint8(np.where((image[:, :, 2] < 240)&(image[:, :, 2] > 200)&(image[:, :, 0] < 75)&(image[:, :, 1] < 70),1,0)) * 128
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    ellps = []
    cnt_ret = []
    for cnt in contours:
        if cnt.shape[0] < 10: 
            continue
        cnt *= scale
        ellp = cv2.fitEllipse(cnt)
        ellps.append(ellp)
        cnt_ret.append(cnt)
        
    return thresh, cnt_ret, ellps

class FRAME():
    def __init__(self, img, binary, R, pos, scale = 2, thresh = 20.0):
        self.img = img
        self.binary = binary
        self.R = R
        self.pos = pos
        self.thresh = thresh
        
        self.R_inv = np.linalg.inv(self.R)
        
        results = get_ellp(self.binary, scale = scale)
        cnts, ellps = results[1], results[2]
        self.ch, _ = self.get_ch(ellps)
        if self.ch != -1:
            self.cnt = np.float32(cnts[self.ch][:, 0])
            self.cnt_origin = np.float32(ellps[self.ch][0])
            self.ellp = ellps[self.ch]
        #print(ellps[ch])
        
    def get_ch(self, ellps):
        if len(ellps) == 0: return -1, -1
        len_a = np.zeros(len(ellps), np.float32)
        for idx, ellp in enumerate(ellps):
            len_a[idx] = ellp[1][0] if ellp[1][0] > ellp[1][1] else ellp[1][1]
        idxs = np.argsort(len_a)
        #print(idxs, len_a[idxs[-1]])
        if len_a[idxs[-1]] < self.thresh: return -1, -1
        for idx_o in range(len(ellps)-1, -1, -1):
            if len_a[idxs[idx_o]] < self.thresh: break
            origin_o = np.float32(ellps[idxs[idx_o]][0])
            for idx_i in range(idx_o - 1, -1, -1):
                if len_a[idxs[idx_i]] < self.thresh: break
                diff = origin_o - np.float32(ellps[idxs[idx_i]][0])
                #print('-------', np.sqrt(np.sum(diff*diff)))
                #print(ellps[idxs[idx_o]])
                #print(ellps[idxs[idx_i]])
                if np.sqrt(np.sum(diff*diff)) < int(len_a[idxs[idx_o]] / 100) * 5 + 5:
                    return idxs[idx_o], idxs[idx_i]
        return -1, -1

    def w2c(self, sfm, pts_w):
        return sfm.w2c(pts_w, self.R_inv, -self.pos)
        
    def w2p(self, sfm, pts_w):
        return sfm.w2p(pts_w, self.R_inv, -self.pos)
        
    def p2w(self, sfm, pts_pix, z_pix):
        return sfm.p2w(pts_pix, z_pix, self.R, self.pos)
    
    def p2w_v2(self, sfm, pts_pix):
        ABCD = sfm.get_ABCD(self.R_inv, -self.pos)
        return sfm.p2w_v2(pts_pix, self.R, self.pos, ABCD)

from circle_fit import calc_t
def p2w_w2p_once(sfm, frame, wt):
    origin_, vec_, yaw_, theta, radius = calc_circle(wt)
    sfm.update_sfm(origin_, vec_, yaw_)
    #outer, _ = init_circle(sfm.origin, radius, sfm.vec, sfm.yaw, theta)
    outer, _ = init_circle(sfm.origin, 0.78, sfm.vec, sfm.yaw, theta)
    cam_, pix_, img_ = frame.w2p(sfm, outer)
    #z_ = calc_tz(frame.cnt, pix_) # this way is not right
    z_ = calc_t(frame.cnt, pix_)[2]
    wt = frame.p2w(sfm, frame.cnt, pix_[:, 2:] + z_)
    return wt