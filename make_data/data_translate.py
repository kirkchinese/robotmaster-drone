import cv2 
import numpy as np
import glob 
import os
img_dir = glob.glob("/home/misaka/drone/nn/dataset/output/*.png")
output_dir = "/home/misaka/drone/nn/dataset/output/"
for img_path in img_dir:
    img = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
    img = np.array(img)
    img = img/128
    output_path = os.path.join(output_dir, os.path.basename(img_path))
    cv2.imwrite(output_path, img)
