import numpy as np
import cv2

def line2p(x0, x1, t):
    return (x0[0] + t * (x1[0] - x0[0]), x0[1] + t * (x1[1] - x0[1]))

def line2p_x(x0, x1, xt):
    t = (xt - x0[0])/ (x1[0] - x0[0])
    return x0[1] + t * (x1[1] - x0[1])

def line2p_y(x0, x1, yt):
    t = (yt - x0[1])/ (x1[1] - x0[1])
    return x0[0] + t * (x1[0] - x0[0])

def update_pt_x(left, right, X):
    for idx in range(X.shape[1]):
        X[0, idx, 1] = line2p_x(left, right, X[0, idx, 0])
        
def update_pt_y(left, right, X):
    for idx in range(X.shape[1]):
        X[0, idx, 0] = line2p_y(left, right, X[0, idx, 1])
        
def update_pt(left, right, X):
    if abs(left[0] - right[0]) > abs(left[1] - right[1]):
        update_pt_x(left, right, X)
    else:
        update_pt_y(left, right, X)
        
def init_pt2(x0, x1, step):
    return np.concatenate([np.float32(line2p(x0, x1, idx * step)).reshape([1, -1, 2]) for idx in range(1, int(1 / step))], axis = 1)

def init_pt(height, width, num):
    wd_r = np.arange(0, width, int(width / num))[1:]
    ht_r = np.arange(0, height, int(height / num))[1:]
    up = np.concatenate([wd_r, np.zeros_like(wd_r)]).reshape([1, 2, -1]).transpose((0, 2, 1)).astype(np.float32)
    down = np.concatenate([wd_r, np.ones_like(wd_r) * (height - 1)]).reshape([1, 2, -1]).transpose((0, 2, 1)).astype(np.float32)
    left = np.concatenate([np.zeros_like(ht_r), ht_r]).reshape([1, 2, -1]).transpose((0, 2, 1)).astype(np.float32)
    right = np.concatenate([np.ones_like(ht_r) * (width - 1), ht_r]).reshape([1, 2, -1]).transpose((0, 2, 1)).astype(np.float32)
    return up, down, left, right

def drawMatches(imageA, imageB, kpsA, kpsB, text = False):
    # initialize the output visualization image
    (hA, wA) = imageA.shape[:2]
    (hB, wB) = imageB.shape[:2]
    vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")
    vis[0:hA, 0:wA] = imageA
    vis[0:hB, wA:] = imageB

    # loop over the matches
    for idx in range(kpsA.shape[1]):
        ptA = (int(kpsA[0][idx][0]), int(kpsA[0][idx][1]))
        ptB = (int(kpsB[0][idx][0]) + wA, int(kpsB[0][idx][1]))
        if text:
            cv2.putText(vis,str(idx), ptA, cv2.FONT_HERSHEY_COMPLEX, 3, (100,255,0), 1, cv2.LINE_AA)
        cv2.line(vis, ptA, ptB, (0, 255, 0), 3)
    return vis