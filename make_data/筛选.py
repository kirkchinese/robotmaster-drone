import cv2
import glob
import os
import numpy as np

def get_binary_yellow(image):
    """
        将输入图像进行预处理，通过深度学习模型进行预测，并返回二值化结果。
        他喵的，改了半天才发现根本没用到这个函数，我日了狗
    """
    yellow_mask = np.logical_and.reduce([
    image[:, :, 2] > 195 , image[:, :, 2] < 240,  # 红色通道的值大于200
    image[:, :, 1] > 30 , image[:, :, 1] < 240,  # 绿色通道的值大于200
    image[:, :, 0] > 30 , image[:, :, 0] < 240,  # 蓝色通道的值小于150
    ])
    yellow_image = np.uint8(yellow_mask) * 128
    # img = np.uint8(np.logical_and(image[:, :, 2] < 240, image[:, :, 2] > 195)) * 128
    return yellow_image


# 获取两个目录中所有图片的文件名
dir1 = "/home/misaka/drone/keyboard_ctrl_ws/data/img/"  # 输入
dir2 = "/home/misaka/drone/keyboard_ctrl_ws/data/new_data/org/"  # 输出1
dir3 = "/home/misaka/drone/keyboard_ctrl_ws/data/new_data/binary/" # 输出2

image_paths1 = glob.glob(os.path.join(dir1, "*.png"))  # 替换为你的图片文件扩展名


# # 循环显示图片
# for image_path1 in image_paths1:
#     # 读取图片
#     img1 = cv2.imread(image_path1)
#     img2 = get_binary_yellow(img1)

#     # 显示图片
#     cv2.imshow("Image 1", img1)
#     cv2.imshow("Image 2", img2)

#     # 等待用户按键
#     key = cv2.waitKey(0)

#     # 如果用户按下A键，则进入下一张图片的显示
#     if key == ord("a"):
#         continue

#     # 如果用户按下X键，则删除图片
#     elif key == ord("x"):
#         os.remove(image_path1)

# # 销毁所有窗口
# cv2.destroyAllWindows()


# 按顺序重输出文件
i=0
for image_path1 in image_paths1:
    img1 = cv2.imread(image_path1)
    cv2.imwrite(os.path.join(dir2, f"img{i}.png"), img1)
    img2 = get_binary_yellow(img1)

    cv2.imshow("Image 1", img1)
    cv2.imshow("Image 2", img2)
    cv2.waitKey(10)
    cv2.imwrite(os.path.join(dir3, f"img{i}.png"), img2)
    i+=1
cv2.destroyAllWindows()

