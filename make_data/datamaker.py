import cv2
import numpy as np
import glob
import os

# 全局变量
drawing = False  # 如果鼠标按下，则为真
ix, iy = -1, -1  
ref_points = []  

# 鼠标回调函数
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, ref_points


    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 1)
            cv2.imshow('image', img_copy)


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
        ref_points.append([(ix, iy), (x, y)])
        cv2.imshow('image', img)

# 获取所有二值化图像的文件路径
image_paths = glob.glob("/home/misaka/drone/keyboard_ctrl_ws/data/new_data/binary/*.png")  # 替换为你的图像文件夹路径
image_paths_binary = "/home/misaka/drone/keyboard_ctrl_ws/data/new_data/org/" 
# 指定保存修改后图像的目录
output_dir = '/home/misaka/drone/keyboard_ctrl_ws/data/new_data/new_binary/'
os.makedirs(output_dir, exist_ok=True)

for image_path in image_paths:
    # 读取二值化图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img1 = cv2.imread((image_paths_binary + os.path.basename(image_path)), cv2.IMREAD_COLOR)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectangle)

    # 显示图像
    cv2.imshow('image', img)
    cv2.imshow('image1', img1)


    cv2.waitKey(0)

    # 确保已经选择了至少一个矩形
    if len(ref_points) > 0:

        mask = np.zeros_like(img) * 128

        # 在掩膜上绘制所有矩形区域，将其设为0
        for top_left, bottom_right in ref_points:
            mask[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = 128

        # 将掩膜应用于原图像，保留矩形区域外的元素，其余设为0
        img = cv2.bitwise_and(img, mask)

        # 显示修改后的图像
        cv2.imshow('Modified Image', img)
        cv2.waitKey(0)

        # 保存修改后的图像
        output_path = os.path.join(output_dir, os.path.basename(image_path))
        cv2.imwrite(output_path, img)

    # 清除矩形选择，为下一张图片做准备
    ref_points = []

    # 销毁当前窗口
    cv2.destroyAllWindows()
