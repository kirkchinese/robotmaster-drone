import sys
sys.path.append('/home/misaka/auto_drone/src/yolo_ros/src/yolov10')
from ultralytics import YOLOv10
import cv2
import glob 
import numpy as np
model = YOLOv10("/home/misaka/auto_drone/src/yolo_ros/src/yolov10/runs/detect/train8/weights/best.pt")

def get_binary(image):
    """
        将输入图像进行预处理，通过深度学习模型进行预测，并返回二值化结果。
        他喵的，改了半天才发现根本没用到这个函数，我日了狗
    """
    img = np.uint8(np.logical_and(image[:, :, 2] < 240, image[:, :, 2] > 195)) * 128
    return img

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


imgs = glob.glob("/home/misaka/drone/keyboard_ctrl_ws/data/img/*.png")
imgs2 = "/home/misaka/drone/keyboard_ctrl_ws/data/img/img2/"
img_binary = "/home/misaka/drone/keyboard_ctrl_ws/data/img/img2_binary/"
img_binary_yellow = "/home/misaka/drone/keyboard_ctrl_ws/data/img/img_yello_binary/"

i=0
for img in imgs:
    
    img = cv2.imread(img)
    results = model.predict(img,show=True)

    if results[0].boxes.xyxy.size(0) != 0:
        if cv2.imwrite(imgs2 + f"yolo{i}.png" ,img) :
            i = i+1
            print(f"imges {i} write successfully to :"+ imgs2 + f"yolo{i}.png")
            # img_binary_img = get_binary(img)
            img_binary_img_yellow = get_binary_yellow(img)
            cv2.imwrite(img_binary_yellow + f"yolo{i}.png" ,img_binary_img_yellow)
            # cv2.imwrite(img_binary + f"yolo{i}.png" ,img_binary_img)
            # cv2.imshow("img_red",img_binary_img)
            cv2.imshow("img_yellow",img_binary_img_yellow)
            cv2.waitKey(0)

# # img_str = glob.glob("/home/misaka/drone/keyboard_ctrl_ws/data/img/*.png")[0]
# img = cv2.imread("/home/misaka/drone/keyboard_ctrl_ws/data/img/left_imgsave331.png")
# img2 = cv2.imread("/home/misaka/drone/keyboard_ctrl_ws/data/img/left_imgsave200.png")
# img_binary_img_yellow = get_binary_yellow(img)
# img_binary_img_yellow_2 = get_binary_yellow(img2)
# cv2.imshow("img_yellow",img_binary_img_yellow)
# cv2.imshow("img_red",img_binary_img_yellow_2)
# cv2.waitKey(0)


# # new two
# i=0
# for img in imgs:
    
#     img = cv2.imread(img)
#     results = model.predict(img,show=True)

#     if results[0].boxes.xyxy.size(0) != 0:
#         if cv2.imwrite(imgs2 + f"yolo{i}.png" ,img) :
#             i = i+1
#             print(f"imges {i} write successfully to :"+ imgs2 + f"yolo{i}.png")
#             # img_binary_img = get_binary(img)
#             img_binary_img_yellow = get_binary_yellow(img)
#             cv2.imwrite(img_binary_yellow + f"yolo{i}.png" ,img_binary_img_yellow)
#             # cv2.imwrite(img_binary + f"yolo{i}.png" ,img_binary_img)
#             # cv2.imshow("img_red",img_binary_img)
#             cv2.imshow("img_yellow",img_binary_img_yellow)
#             cv2.waitKey(0)
