import cv2
import glob
import os

# 获取两个目录中所有图片的文件名
dir1 = "/home/misaka/drone/keyboard_ctrl_ws/data/data_handmaker/yellow_re/"  # 替换为你的第一个目录路径
dir2 = "/home/misaka/drone/keyboard_ctrl_ws/data/data_handmaker/yellow_binary/"  # 替换为你的第二个目录路径

image_paths1 = glob.glob(os.path.join(dir1, "*.png"))  # 替换为你的图片文件扩展名
image_paths2 = glob.glob(os.path.join(dir2, "*.png"))  # 替换为你的图片文件扩展名

# 确保两个目录中的图片数量相同
assert len(image_paths1) == len(image_paths2), "两个目录中的图片数量不同！"

# 循环显示图片
for image_path1, image_path2 in zip(image_paths1, image_paths2):
    # 读取图片
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)

    # 显示图片
    cv2.imshow("Image 1", img1)
    cv2.imshow("Image 2", img2)

    # 等待用户按键
    key = cv2.waitKey(0)

    # 如果用户按下A键，则进入下一张图片的显示
    if key == ord("a"):
        continue

    # 如果用户按下X键，则删除两张图片
    elif key == ord("x"):
        os.remove(image_path1)
        os.remove(image_path2)

# 销毁所有窗口
cv2.destroyAllWindows()
