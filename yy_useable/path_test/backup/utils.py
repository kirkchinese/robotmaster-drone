import numpy as np
import cv2
import matplotlib.pyplot as plt

def _find_min(pt, origin, theta, cur_pos, win):
    idxs = np.zeros(2 * win + 1, np.int32)
    start = cur_pos - win
    idxs = (np.arange(2 * win + 1) + start) % pt.shape[0]
    diff = pt[idxs] - origin.reshape([1, -1])
    dist = np.abs(np.cos(theta) * diff[:, 1] - np.sin(theta) * diff[:, 0])
    _ch = np.argmin(dist)
    #print(idxs, idxs[_ch], pt[idxs[_ch]])
    #print(pt[idxs].T)
    #print(theta, dist)
    return idxs[_ch], pt[idxs[_ch]]

def _get_theta(pt, origin):
    return np.arctan2(pt[:, 1] - origin[1], pt[:, 0] - origin[0])

def match_ellp_aux(rept, theta, pt, origin, win = 3):
    rept = rept.copy()
    pt_m = np.zeros_like(rept)
    start = np.argmin(rept[:, 1])
    cur_ch = np.argmin(pt[:, 1])
    rept = rept - rept[start:start+1] + pt[cur_ch:cur_ch+1]
    idxs = np.zeros(rept.shape[0], np.int32)
    pt_m[start, :], idxs[start] = pt[cur_ch], cur_ch
    for idx in range(start-1, start - rept.shape[0], -1):
        #print(idx, "++++++++++++++++++++==", rept[idx])
        cur_ch, pt_m[idx, :] = _find_min(pt, origin, theta[idx], cur_ch, win = win)
        idxs[idx] = cur_ch
    return pt_m, idxs

def match_ellp2(rept, pt):
    l1, l2 = rept.shape[0], pt.shape[0]
    start = np.argmin(rept[:, 1])
    cur_ch = np.argmin(pt[:, 1])
    idxs = (np.int32(np.arange(l1) / (l1 - 1) * (l2-1)) + cur_ch) % l2
    pt_m = np.zeros_like(rept)
    pt_m[start:] = pt[idxs[0:l1-start]]
    pt_m[0:start] = pt[idxs[l1-start:]]
    return pt_m, idxs

def get_ellp(image): 
    thresh = np.uint8(np.logical_and(image[:, :, 2] < 240, image[:, :, 2] > 220)) * 128
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    ellps = []
    cnt_ret = []
    for cnt in contours:
        if cnt.shape[0] < 10: 
            continue
        ellp = cv2.fitEllipse(cnt)
        ellps.append(ellp)
        cnt_ret.append(cnt)
        
    return thresh, cnt_ret, ellps

def w2p_init(sfm, frame1, frame2, origin, yaw, draw = False):
    sfm.origin, sfm.yaw = origin, yaw
    sfm.init_circle()
    
    frame1.w2p_v2(sfm)
    frame2.w2p_v2(sfm)

    if draw:
        img1 = frame1.draw_circle()
        img2 = frame2.draw_circle()
        plt.subplot(121)
        plt.imshow(img1)
        plt.subplot(122)
        plt.imshow(img2)
        plt.show()