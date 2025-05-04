import cv2
import numpy as np
import glob
import os

# 全局变量
drawing = False  # 如果鼠标按下，则为真
ix, iy = -1, -1  # 初始鼠标位置
ref_point = []  # 用于存储矩形的两个角点

# 鼠标回调函数
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, ref_point

    # 当鼠标按下时，记录起始位置，并设置drawing为True
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # 当鼠标移动时，如果drawing为True，则绘制矩形
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 1)
            cv2.imshow('image', img_copy)

    # 当鼠标释放时，记录结束位置，并设置drawing为False
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)
        ref_point = [(ix, iy), (x, y)]
        cv2.imshow('image', img)

# 获取所有二值化图像的文件路径
image_paths = glob.glob("/home/misaka/drone/keyboard_ctrl_ws/data/img/img_yello_binary/*.png")  # 替换为你的图像文件夹路径

# 指定保存修改后图像的目录
output_dir = '/home/misaka/drone/keyboard_ctrl_ws/data/data_handmaker/'
os.makedirs(output_dir, exist_ok=True)

for image_path in image_paths:
    # 读取二值化图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # 创建一个窗口并绑定鼠标回调函数
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectangle)

    # 显示图像
    cv2.imshow('image', img)

    # 等待用户绘制矩形
    cv2.waitKey(0)

    # 确保已经选择了矩形
    if len(ref_point) == 2:
        # 获取矩形的角点
        top_left, bottom_right = ref_point

        # 找到图像中的所有圆环
        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)

        # 如果没有找到圆环，跳过当前图像
        if circles is None:
            continue

        # 创建一个与原图像大小相同的掩膜，所有元素初始为0
        mask = np.zeros_like(img)

        # 遍历所有圆环
        for circle in circles[0]:
            # 获取圆环的中心和半径
            cx, cy, radius = circle
            # 检查圆环是否在矩形区域内
            if top_left[0] <= cx <= bottom_right[0] and top_left[1] <= cy <= bottom_right[1] and \
               top_left[0] <= cx + radius <= bottom_right[0] and top_left[1] <= cy + radius <= bottom_right[1]:
                # 在掩膜上绘制该圆环
                cv2.circle(mask, (int(cx), int(cy)), int(radius), 255, thickness=cv2.FILLED)

        # 将掩膜应用于原图像，只保留矩形区域内的圆环
        img = cv2.bitwise_and(img, mask)

        # 显示修改后的图像
        cv2.imshow('Modified Image', img)
        cv2.waitKey(0)

        # 保存修改后的图像
        output_path = os.path.join(output_dir, os.path.basename(image_path))
        cv2.imwrite(output_path, img)

    # 清除矩形选择，为下一张图片做准备
    ref_point = []

    # 销毁当前窗口
    cv2.destroyAllWindows()
