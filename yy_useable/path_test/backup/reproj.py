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

def sloveAx(A):
    A = np.concatenate([A, np.ones([A.shape[0], 1], A.dtype)], axis = 1)
    u,sigma,v = np.linalg.svd(A)
    return v[-1]

def KRt2proj(K, R, t):
    proj = np.zeros((3, 4), np.float32)
    proj[0:3, 0:3] = np.float32(R)
    proj[:, 3] = np.float32(t).T
    return np.dot(np.float32(K), proj)

def projection_w2p(pts, K, R, t):
    pts = np.concatenate([pts, np.ones([pts.shape[0], 1], pts.dtype)], axis = 1)
    proj = KRt2proj(K, R, t)
    p3d = proj.dot(pts.T).T
    return p3d[:, 0:2] / p3d[:, 2:]

def projection_w2c(pts, R, t):
    pts = np.concatenate([pts, np.ones([pts.shape[0], 1], pts.dtype)], axis = 1)
    proj = KRt2proj(np.eye(3), R, t)
    p3d = proj.dot(pts.T).T
    return p3d

'''
p1 = np.float32([[81.89029394, 234.42333861]])
p2 = np.float32([[-10.91335538, 230.51641358]])
p3d_self = triangulatePoints_np(p1[0], p2[0], KRT_57, KRT_61)
pt4d = cv2.triangulatePoints(KRT_57, KRT_61, p1.T, p2.T)
print(p3d_self.T, pt4d.T)
'''
def triangulatePoints_np(kp1, kp2, Proj1, Proj2):
    A0 = np.mat(kp1[0] * Proj1[2,:] - Proj1[0,:])
    A1 = np.mat(kp1[1] * Proj1[2,:] - Proj1[1,:])
    A2 = np.mat(kp2[0] * Proj2[2,:] - Proj2[0,:])
    A3 = np.mat(kp2[1] * Proj2[2,:] - Proj2[1,:])
    train_data = np.mat(np.vstack((A0,A1,A2,A3)))
    U,sigma,VT = np.linalg.svd(train_data)
    posx = VT[3,:].T
    return posx

#事实上这个最小二次误差的解是有几何上的含义的,也就是两条直线公垂线的中点。
'''
def reconstruct(K, R1, T1, R2, T2, p1, p2):
    proj1 = np.zeros((3, 4))
    proj2 = np.zeros((3, 4))
    proj1[0:3, 0:3] = np.float32(R1)
    proj1[:, 3] = np.float32(T1.T)
    proj2[0:3, 0:3] = np.float32(R2)
    proj2[:, 3] = np.float32(T2.T)
    fk = np.float32(K)
    proj1 = np.dot(fk, proj1)
    proj2 = np.dot(fk, proj2)
    pt4d = cv2.triangulatePoints(proj1, proj2, p1.T, p2.T).T
    return pt4d[:, 0:3] / pt4d[:, 3:]
'''

def reconstruct(K, R1, T1, R2, T2, p1, p2):
    proj1 = KRt2proj(K, R1, T1)
    proj2 = KRt2proj(K, R2, T2)
    pt4d = cv2.triangulatePoints(proj1, proj2, p1.T, p2.T).T
    return pt4d[:, 0:3] / pt4d[:, 3:]

def angle_vec(vec1, vec2):
    norm = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    cos_ = np.dot(vec1, vec2) / norm
    sin_ = np.cross(vec1, vec2) / norm
    return np.arctan2(sin_[-1], cos_)

def calc_circle(pt3d):
    origin = np.mean(pt3d, axis = 0)
    ABD = sloveAx(pt3d[:, 0:2])
    vec1 = np.float32([1, 0, 0])
    vec2 = np.float32([ABD[0], ABD[1], 0.0])
    yaw = angle_vec(vec1, vec2)
    #R = rodrigues([0, 0, 1], yaw)
    #print(vec2 / np.linalg.norm(vec2), R.dot(vec1))
    return origin.reshape([1, -1]), yaw

def rec_sim(KRt1, KRt2, p1, p2): 
    pt4d = cv2.triangulatePoints(KRt1, KRt2, p1.T, p2.T).T
    return pt4d[:, 0:3] / pt4d[:, 3:]

def w2p_sim(KRt, pts):
    pts = np.concatenate([pts, np.ones([pts.shape[0], 1], pts.dtype)], axis = 1)
    p3d = KRt.dot(pts.T).T
    return p3d[:, 0:2] / p3d[:, 2:]

#wt = rec_v2(np.linalg.inv(sfm.CK), frame_57.R, frame_57.pos + sfm.CAM_T, frame_57.inner_img, frame_57.inner_pix[:, 2:])
#print(wt[0], sfm.inner[0])
def rec_v2(K_, R_, t_, pt, z_pix):
    p3d = np.concatenate([pt * z_pix, z_pix], axis = 1)
    #cam = K_.dot(p3d.T)
    #wt = R_.dot(cam + t_.reshape([-1, 1])).T
    return R_.dot(K_.dot(p3d.T) + t_.reshape([-1, 1])).T

def init_circle(origin, vec, yaw, length):
    theta = np.arange(length) * 2 * np.pi / length - np.pi
    inner = np.zeros([length, 3], np.float32)
    outer = np.zeros([length, 3], np.float32)
    inner_r, outer_r = 0.6, 0.78
    inner[:, 1] = inner_r * np.cos(theta)
    inner[:, 2] = inner_r * np.sin(theta)
    outer[:, 1] = outer_r * np.cos(theta)
    outer[:, 2] = outer_r * np.sin(theta)
    
    rot = rodrigues(vec, yaw)
    
    inner = rot.dot(inner.T).T + np.float32(origin).reshape(1, 3)
    outer = rot.dot(outer.T).T + np.float32(origin).reshape(1, 3)
    return inner, outer

class SFM():
    def __init__(self, LENGTH_SAMPLE = 100):
        self.origin, self.yaw = np.zeros([1, 3], np.float32), 0.0
        self.inner, self.outer = [], []
        self.LENGTH_SAMPLE = LENGTH_SAMPLE
        self.LEFT_CAM_T = np.float32([0.26, -0.0475, 0.0])
        #self.RIGHT_CAM_T = np.float32([0.26, 0.0475, 0.0])
        self.CAM_K = np.float32([[320, 0, 320], [0, 320,  240], [0, 0, 1]])
        self.CAM_T = np.float32([0.26, -0.0475, 0.0])
        self.Rw2c = np.float32([[0, 1, 0], [0, 0, -1], [1, 0, 0]])
        self.CK = self.CAM_K.dot(self.Rw2c)
        self.CK_inv = np.linalg.inv(self.CK)
        self.SIZE = (640, 480)
        
    def init_circle(self):
        self.inner, self.outer = init_circle(self.origin, [0, 0, 1], self.yaw, self.LENGTH_SAMPLE)
        
    def w2c(self, R, t): # R, t. 相机姿态 same as world
        inner_cam = projection_w2c(self.inner, R, t - self.CAM_T)
        outer_cam = projection_w2c(self.outer, R, t - self.CAM_T)
        origin_cam = projection_w2c(self.origin.reshape([1, -1]), R, t - self.CAM_T)
        return inner_cam, outer_cam, origin_cam
        
    def w2p(self, R, t): # R, t. 相机姿态
        inner_img = projection_w2p(self.inner, self.CK, R, t - self.CAM_T)
        outer_img = projection_w2p(self.outer, self.CK, R, t - self.CAM_T)
        origin_img = projection_w2p(self.origin, self.CK, R, t - self.CAM_T)
        return inner_img, outer_img, origin_img

    def w2p_v2(self, R, t):
        inner_cam, outer_cam, origin_cam = self.w2c(R, t)
        inner_pix = self.CK.dot(inner_cam.T).T 
        outer_pix = self.CK.dot(outer_cam.T).T
        origin_pix = self.CK.dot(origin_cam.T).T
        inner_img = inner_pix[:, 0:2] / inner_pix[:, 2:]
        outer_img = outer_pix[:, 0:2] / outer_pix[:, 2:]
        origin_img = origin_pix[:, 0:2] / origin_pix[:, 2:]
        return inner_pix, outer_pix, origin_pix, inner_img, outer_img, origin_img
    
    def p2w(self, R_, t_, pt, z_pix):
        p3d = np.concatenate([pt * z_pix, z_pix], axis = 1)
        return R_.dot(self.CK_inv.dot(p3d.T) + (t_ + self.CAM_T).reshape([-1, 1])).T

from utils import match_ellp_aux, get_ellp, _get_theta, match_ellp2
class FRAME():
    def __init__(self, img, R, pos, thresh = 20.0):
        self.img = img
        self.R = R
        self.pos = pos
        self.thresh = thresh
        
        self.R_inv = np.linalg.inv(self.R)
        
        results = get_ellp(self.img)
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
        
    def match_ellp(self):
        win_size = self.cnt.shape[0] // self.outer_img.shape[0]
        win_size = 3 * (win_size if win_size > 3 else 3)
        self.theta = _get_theta(self.outer_img, self.origin_img[0])
        self.ellp_m, self.idxs = match_ellp_aux(self.outer_img, self.theta, self.cnt, self.cnt_origin, win = win_size)
        
    def match_ellp2(self):
        self.ellp_m, self.idxs = match_ellp2(self.outer_img, self.cnt)
        
    def w2c(self, sfm):
        self.inner_cam, self.outer_cam, self.origin_cam = sfm.w2c(self.R_inv, -self.pos)
        
    def w2p(self, sfm):
        self.inner_img, self.outer_img, self.origin_img = sfm.w2p(self.R_inv, -self.pos)
        
    def w2p_v2(self, sfm):
        self.inner_pix, self.outer_pix, self.origin_pix, self.inner_img, self.outer_img, self.origin_img = \
            sfm.w2p_v2(self.R_inv, -self.pos)
        
    def p2w(self, sfm):
        return sfm.p2w(self.R, self.pos, self.ellp_m, self.outer_pix[:, 2:])
    
    def draw_circle(self):
        img = cv2.drawContours(self.img.copy(), [np.int32(self.inner_img)], -1, (0,255,0), 3)
        img = cv2.drawContours(img, [np.int32(self.outer_img)], -1, (0,255,0), 3)
        return img