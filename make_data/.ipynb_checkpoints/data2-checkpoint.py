import cv2
import glob 
import numpy as np

imgs = glob.glob("/home/misaka/drone/keyboard_ctrl_ws/data/img/img_yello_binary/*.png")
imgstr = "/home/misaka/drone/keyboard_ctrl_ws/data/img/imgtry/"
imgstr_eroded_img = "/home/misaka/drone/keyboard_ctrl_ws/data/img/imgtry/eroded_img"
imgstr_dilated_img = "/home/misaka/drone/keyboard_ctrl_ws/data/img/imgtry/dilated_img"
imgstr_opened_img = "/home/misaka/drone/keyboard_ctrl_ws/data/img/imgtry/opened_img"
imgstr_top_hat_img = "/home/misaka/drone/keyboard_ctrl_ws/data/img/imgtry/top_hat_img"



kernel = np.array(([0, 1, 0],
                  [1, 1, 1],
                  [0, 1, 0]), dtype=np.uint8)

i=0
for img in imgs:
    
    img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)

    eroded_image = cv2.erode(img, kernel, iterations=1)
    dilated_image = cv2.dilate(img, kernel, iterations=1)
    opened_image = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    # top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
    closed_image = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("img",img)
    cv2.imshow("eroded_img",eroded_image)
    cv2.imshow("dilated_img",dilated_image)
    cv2.imshow("opened_img",opened_image)
    # cv2.imshow("top_hat",top_hat)
    cv2.imshow('Closed Image', closed_image)

    # cv2.imwrite(imgstr + f"yolo{i}.png" ,img)
    # cv2.imwrite(imgstr_eroded_img + f"yolo{i}.png" ,eroded_image)
    # cv2.imwrite(imgstr_dilated_img + f"yolo{i}.png" ,dilated_image)
    # cv2.imwrite(imgstr_opened_img + f"yolo{i}.png" ,opened_image)
    # cv2.imwrite(imgstr_top_hat_img + f"yolo{i}.png" ,top_hat)
    # print(f"imges {i} write successfully to :"+ imgstr + f"yolo{i}.png")
    i = i+1

    cv2.waitKey(0)