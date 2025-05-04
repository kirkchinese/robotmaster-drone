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