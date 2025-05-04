import numpy as np
import cv2
def rodrigues(vec, theta):
    """
        Rodrigues旋转公式是一种用于将旋转向量转换为旋转矩阵的数学方法。
        在给定的代码中，Rodriguess函数以旋转向量vec和角度θ为输入，并返回相应的旋转矩阵。
    """
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
    """
        该类表示一个SFM（Simultaneous Localization and Mapping）系统
        它包含了相机的内在矩阵、外在矩阵、旋转矩阵和平移向量等属性
        它还包含了一些函数来执行世界坐标系和相机坐标系之间的转换
    """
    
    def __init__(self, origin, vec, yaw):
        """
            初始化:在创建SFM类的实例时,将会调用__init__方法来进行初始化。
            在此方法中,将定义相机的
            内在矩阵(CAM_K)、
            外在矩阵(CAM_T)、
            从世界到相机的旋转矩阵(Rw2c)、
            相机矩阵(CK)和相机的分辨率(SIZE)。
            在此方法中,还会调用update_sfm方法来更新SFM系统的原点、偏航角和向量。
        """
        self.CAM_K = np.float32([[320, 0, 320], 
                                 [0, 320,  240], 
                                 [0, 0, 1]])
        """
            固有相机矩阵是一个3x3矩阵，包含相机的内部参数，如焦距、主点和偏斜系数。
            这些值表示分辨率为640x480像素的相机的典型固有相机矩阵，其中主点位于图像的中心，焦距在x和y方向上都是相同的。
            最后一行[0,0,1]表示齐次坐标系。
            固有相机矩阵对于相机校准过程至关重要，该过程涉及估计相机的内部参数。
            它用于各种计算机视觉算法，如3D重建、姿态估计和图像处理任务。
        """
        self.CAM_T = np.float32([0.26, 
                                 -0.0475,
                                   0.0])
        """
            self.CAM_T 是一个 numpy 数组，它表示相机的外在参数，即相机的平移向量。
            在本例中，相机的平移向量被设置为 [0.26, -0.0475, 0.0]。
        """
        self.Rw2c = np.float32([[0, 1, 0], 
                                [0, 0, 1], 
                                [1, 0, 0]])
        """
            self.Rw2c，相机的外在参数包括相机的位置（平移向量）和相机的姿态（旋转矩阵）。
            在本代码中，相机的旋转矩阵 self.Rw2c 被设置为
            [0, 1, 0]
            [0, 0, 1]
            [1, 0, 0]
            这是一个单位矩阵，表示相机的姿态是默认的，即相机的正前方是 x 轴正方向，向上是 y 轴正方向，向右是 z 轴正方向。
        """
        self.CK = self.CAM_K.dot(self.Rw2c)
        """
            self.CK 是相机矩阵，它是固有相机矩阵和旋转矩阵的乘积。
        """
        self.CK_inv = np.linalg.inv(self.CK)
        """
            self.CK_inv 是相机矩阵 CK 的逆矩阵。
        """
        self.SIZE = (640, 480)
        """
            self.SIZE 是一个元组
            它表示相机的分辨率，在本例中被设置为 (640, 480)
            表示相机的分辨率为 640x480 像素
        
        """
        
        self.update_sfm(origin, vec, yaw)
        
    def update_sfm(self, origin, vec, yaw):
        """
            更新SFM（update_sfm）：在此方法中，将更新SFM系统的原点、偏航角和向量。
            它还会通过将向量[1, 0, 0]应用于旋转矩阵来计算ABC向量。
        """
        self.origin, self.yaw, self.vec = origin, yaw, vec
        self.ABC = rodrigues(vec, yaw).dot(np.float32([[1], [0], [0]]))
    
    def w2c(self, pts, R, t): # R, t. 相机姿态 same as world, cam = R.dot(x + t)
        """
            世界到相机（w2c）：在此方法中，将3D点从世界坐标系转换到相机坐标系。
            它使用旋转矩阵R和平移向量t来实现此操作。
        """ 
        return R.dot((pts + (t - self.CAM_T).reshape([1, -1])).T).T
    
    
    def get_ABCD(self, R, t):
        """
            获取ABCD（get_ABCD）：在此方法中，将根据相机的原点和旋转矩阵来计算平面方程的系数ABCD。
            它首先将世界坐标系中的原点转换到相机坐标系，然后将旋转矩阵应用于向量[1, 0, 0]来得到ABC向量。
            最后，将ABC向量与相机坐标系中的原点的负内积连接起来，得到ABCD向量。
        """
        origin_cam = self.w2c(self.origin.reshape([1, -1]), R, t)
        ABC = R.dot(self.ABC)
        return np.concatenate([ABC, -origin_cam.dot(ABC)], axis = 0)
    
    
    def w2p(self, pts, R, t): #cam = R.dot(x + t)
        """
            世界到像素（w2p）：在此方法中，将3D点从世界坐标系转换到像素坐标系。
            它首先使用w2c方法将点转换到相机坐标系，然后将相机矩阵CK应用于相机坐标系中的点来得到像素坐标。
        """
        cam = self.w2c(pts, R, t)
        pix = self.CK.dot(cam.T).T 
        img  = pix[:, 0:2] / pix[:, 2:]
        return cam, pix, img


    
    def p2w(self, pts, z_pix, R_, t_): #cam = R.dot(x + t)
        p3d = np.concatenate([pts * z_pix, z_pix], axis = 1)
        return R_.dot(self.CK_inv.dot(p3d.T)).T + (t_ + self.CAM_T).reshape([1, -1])
    """
        像素到世界（p2w）：在此方法中，将像素坐标从像素坐标系转换到世界坐标系。
        它首先将像素坐标应用于相机矩阵的逆矩阵，然后使用旋转矩阵R_和平移向量t_来实现此操作。
    
    """
    
    def p2w_v2(self, pts, R_, t_, ABCD): #cam = R.dot(x + t)
        z_pix = np.ones([pts.shape[0], 1], np.float32)
        pix_ = np.concatenate([pts, z_pix], axis = 1)
        cam_ = self.CK_inv.dot(pix_.T)
        z_pix[:, 0] = -ABCD[3, 0] / (ABCD[0:3].T.dot(cam_))
        return R_.dot(cam_ * z_pix.T).T + (t_ + self.CAM_T).reshape([1, -1])
    """
        像素到世界（版本2）（p2w_v2）：在此方法中，是对p2w方法的一种优化。
        它使用get_ABCD方法中得到的ABCD向量来计算像素点的深度。
        这可以避免对每个点单独计算深度，从而提高性能，特别是在处理大数据集时。
    
    """
def get_ellp(thresh, scale = 2): 
    """
        该函数的主要功能是在二值图像中检测轮廓，并对每个轮廓进行缩放和椭圆拟合，最终返回检测到的椭圆参数和调整后的轮廓点。
        需要注意的是，这段代码依赖于 OpenCV 库，因此在运行前需要确保已安装该库。
        get_ellp 的函数，用于在二值图像 thresh 中检测并拟合椭圆形。
        thresh 是一个二值图像，scale 是一个可选参数，用于缩放检测到的轮廓。
         
    """
    #thresh = np.uint8(np.logical_and(image[:, :, 2] < 240, image[:, :, 2] > 220)) * 128
    #thresh = np.uint8(np.logical_and(image[:, :, 2] < 215, image[:, :, 2] > 195)) * 128
    #thresh = np.uint8(np.logical_and(image[:, :, 2] < 240, image[:, :, 2] > 195)) * 128
    #thresh = np.uint8(np.where((image[:, :, 2] < 240)&(image[:, :, 2] > 200)&(image[:, :, 0] < 75)&(image[:, :, 1] < 70),1,0)) * 128
    """
        这些注释掉的代码行展示了如何生成二值图像 thresh。
        它们使用不同的条件来提取图像中的特定区域，并将其转换为二值图像。
        这些条件通常基于图像的某些颜色通道的值。
    """
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    # 使用 OpenCV 的 findContours 函数检测 thresh 中的轮廓。
    # 1 表示轮廓检索模式，这里使用的是 RETR_EXTERNAL（只检测最外层的轮廓）。
    # 2 表示轮廓近似方法，这里使用的是 CHAIN_APPROX_SIMPLE（只存储轮廓的端点）。

    ellps = []
    # ellps：用于存储检测到的椭圆参数。
    cnt_ret = []
    # cnt_ret：用于存储调整后的轮廓点。

    for cnt in contours:
        if cnt.shape[0] < 10: 
            continue
        cnt *= scale
        ellp = cv2.fitEllipse(cnt)
        ellps.append(ellp)
        cnt_ret.append(cnt)
    # 遍历检测到的每个轮廓 cnt。
    # 如果轮廓点数少于10个，则跳过该轮廓。
    # 将轮廓点坐标乘以缩放因子 scale。
    # 使用 cv2.fitEllipse 函数拟合椭圆，并存储椭圆参数到 ellps 列表。
    # 将调整后的轮廓点添加到 cnt_ret 列表。
    return thresh, cnt_ret, ellps  
    # 返回处理后的二值图像 thresh。
    # 返回调整后的轮廓点列表 cnt_ret。
    # 返回检测到的椭圆参数列表 ellps。


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