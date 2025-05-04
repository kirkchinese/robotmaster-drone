import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from reproj import init_circle
def plot3d(pt):
    x, y, z = pt[:, 0], pt[:, 1], pt[:, 2]
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    #不显示坐标轴
    #ax.set_xticks([])
    #ax.set_yticks([])
    #ax.set_zticks([])
    #设置标题
    ax.set_title("3D_Curve")
    ax.grid(False)
    ax.plot(x,y,z,linestyle='',linewidth=1.2,marker='3',markersize=5, alpha=0.8, c='green')
    plt.show()
    
def draw(image, thresh, blank1, blank2):
    plt.figure(figsize=(10,10))
    plt.subplot(221)
    plt.imshow(image)
    plt.subplot(222)
    plt.imshow(thresh)
    plt.subplot(223)
    plt.imshow(blank1)
    plt.subplot(224)
    plt.imshow(blank2)
    plt.show()
    
def draw_cnt(pt, size = (480, 640)):
    blank = np.zeros(size, np.uint8)
    blank = cv2.drawContours(blank, [np.int32(pt)], -1, (0,255,0), 3)
    plt.imshow(blank)
    plt.show()

from reproj import KRt2proj, w2p_sim
import numpy as np
import cv2
def draw_frame(sfm, frame, wt = None, length = 100):
    KRt = KRt2proj(sfm.CK, np.linalg.inv(frame.R), np.linalg.inv(frame.R).dot(-(frame.pos + sfm.CAM_T)))
    theta = np.arange(length) * 2 * np.pi / length - np.pi
    outer, _ = init_circle(sfm.origin, 0.78, sfm.vec, sfm.yaw, theta)
    _, _, outer_img = frame.w2p(sfm, outer)
    img1 = cv2.drawContours(frame.img.copy(), [np.int32(outer_img)], -1, (0,255,255), 3)
    
    if frame.ch != -1:
        img2 = cv2.drawContours(frame.img.copy(), [np.int32(frame.cnt)], -1, (255,0,0), 3)
    else:
        img2 = frame.img
        
    if wt is not None:
        pt2d = w2p_sim(KRt, wt)
        img3 = cv2.drawContours(frame.img.copy(), [np.int32(pt2d)], -1, (0,255,0), 3)
    else:
        img3 = frame.img
    
    plt.figure(figsize = (10, 5))
    plt.subplot(131)
    plt.imshow(img1)
    plt.subplot(132)
    plt.imshow(img2)
    plt.subplot(133)
    plt.imshow(img3)
    plt.show()