import random 
import cv2

img_directory = '/home/misaka/drone/15pass/data/img/'
rpy_file_path = '/home/misaka/drone/15pass/data/front_view.txt'
new_file_path = '/home/misaka/drone/train_net_work/data/front_view.txt'


img_numbers_and_rpy_dis_yaw = []


#获得所有图像编号
with open(rpy_file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(',') 

        # 提取图像编号
        img_number = parts[0]
        # 提取RPY数据
        rpy_part = [eval(parts[1].split('= (')[1]),eval(parts[2]),eval(parts[3][0:-1])]
        #rpy = [float(x) for x in rpy_part]
        distance = eval(parts[4].split('=')[1].strip())
        yaw = eval(parts[5].split('=')[1].strip())

        img_numbers_and_rpy_dis_yaw.append([img_number,rpy_part,distance,yaw])


#打乱图像编号
source_img_numbers = img_numbers_and_rpy_dis_yaw
random.shuffle(img_numbers_and_rpy_dis_yaw)

file = open(new_file_path,'w')

for i in range(0, len(img_numbers_and_rpy_dis_yaw)):
    img = cv2.imread(f'/home/misaka/drone/15pass/data/img/front_view_{img_numbers_and_rpy_dis_yaw[i][0]}.png')
    cv2.imwrite(f'/home/misaka/drone/train_net_work/data/img/front_view_{i}.png', img)
    file.write(f'{i},RPY = ({img_numbers_and_rpy_dis_yaw[i][1][0]},{img_numbers_and_rpy_dis_yaw[i][1][1]},{img_numbers_and_rpy_dis_yaw[i][1][2]}), distance = {img_numbers_and_rpy_dis_yaw[i][2]}, yaw = {img_numbers_and_rpy_dis_yaw[i][3]}\n')
    cv2.imshow("imgfile",img)
    cv2.waitKey(10)
    print(f'{i},RPY = ({img_numbers_and_rpy_dis_yaw[i][1][0]},{img_numbers_and_rpy_dis_yaw[i][1][1]},{img_numbers_and_rpy_dis_yaw[i][1][2]}), distance = {img_numbers_and_rpy_dis_yaw[i][2]}, yaw = {img_numbers_and_rpy_dis_yaw[i][3]}')
print("Done!")



