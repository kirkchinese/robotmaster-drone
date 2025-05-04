import os
import torch
from torch.utils.data import Dataset,DataLoader
import cv2



class DroneDataset(Dataset):
    def __init__(self, img_dir, rpy_file):
        self.img_dir = img_dir
        self.rpy_file = rpy_file
        self.image_files = []
        self.rpy_data = []
        self.distance_data = []
        self.yaw_data = []
        
        # 读取Rpy数据
        self._load_rpy_data()

    def _load_rpy_data(self):
        with open(self.rpy_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',') 

                # 提取图像编号
                img_number = parts[0]
                # 提取RPY数据
                rpy_part = [eval(parts[1].split('= (')[1]),eval(parts[2]),eval(parts[3][0:-1])]
                #rpy = [float(x) for x in rpy_part]
                distance = eval(parts[4].split('=')[1].strip())
                yaw = eval(parts[5].split('=')[1].strip())
                # 保存数据
                self.image_files.append(f'front_view_{img_number}.png')
                self.rpy_data.append(rpy_part)
                self.distance_data.append(distance)
                self.yaw_data.append(yaw)


    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.image_files[idx])
        image = cv2.imread(img_path)
        # image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 灰度化
        # image_hist = cv2.equalizeHist(image_gray)
        # image_normalized = image_hist.reshape(1, 640, 480) / 255.0 # 为与pytorch中卷积神经网络API的设计相适配,需reshape原图
        # image_tensor = torch.from_numpy(image_normalized)
        # image_tensor = image_tensor.type('torch.FloatTensor') # 指定为'torch.FloatTensor'型,否则送进模型后会因数据类型不匹配而报错
        roll, pitch, yawd = self.rpy_data[idx]    #加上图像img是输入的

        distance = self.distance_data[idx]    #输出的值
        yaw = self.yaw_data[idx]

        # 转换为Tensor
        image_tensor = self.transform(image)
        
        return image, image_tensor, roll, pitch, yawd, distance, yaw


    def transform(self, image):
        # 这里添加数据增强或预处理
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 灰度化
        image_hist = cv2.equalizeHist(image_gray)
        image_normalized = image_hist.reshape(1, 640, 480) / 255.0 # 为与pytorch中卷积神经网络API的设计相适配,需reshape原图
        image_tensor = torch.from_numpy(image_normalized)
        image_tensor = image_tensor.type('torch.FloatTensor') # 指定为'torch.FloatTensor'型,否则送进模型后会因数据类型不匹配而报错
        # 如果需要其他转换,可以在这里添加
        return image_tensor  # 直接返回原图像,可以根据需要进行修改



# 使用示例
if __name__ == "__main__":
    # img_directory = '/home/misaka/drone/15pass/data/img/'
    # rpy_file_path = '/home/misaka/drone/15pass/data/front_view.txt'

    img_directory = '/home/misaka/drone/train_net_work/data/img/'
    rpy_file_path = '/home/misaka/drone/train_net_work/data/front_view.txt'

    dataset = DroneDataset(img_directory, rpy_file_path)
    

    # 测试数据集
    for img,img_tensor,roll,pitch,yawd,distance,yaw in dataset:
        print(type(img_tensor),roll, pitch, yawd, distance, yaw)
        cv2.imshow("img",img)
        cv2.waitKey(20)
        