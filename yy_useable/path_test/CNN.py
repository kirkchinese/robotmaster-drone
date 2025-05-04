from torch import nn
import torch.nn.functional as F
import torch
import cv2
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.layer1 = nn.Sequential( 
               nn.Conv2d(3,7,kernel_size=3, padding = 1) ,
               nn.BatchNorm2d(7),
               nn.MaxPool2d(kernel_size=2 , stride=2),
               nn.ReLU(inplace=True),)

        self.layer2 = nn.Sequential( 
               nn.Conv2d(7,11,kernel_size=3, padding = 1) ,
               nn.BatchNorm2d(11) ,
               #nn.MaxPool2d(kernel_size=2 , stride=2),
               nn.ReLU(inplace=True))

        self.layer3 = nn.Sequential( 
            nn.Conv2d(11,17,kernel_size=3, padding = 1),
            nn.BatchNorm2d(17) ,
            nn.ReLU(inplace=True),
            nn.Conv2d(17,1,kernel_size=3, padding = 1))


    def forward(self , x):
        x = self.layer1(x).to('cuda')
        x = self.layer2(x).to('cuda')
        x = self.layer3(x).to('cuda')
        return x
    
class BCELoss(nn.Module):
    def __init__(self, eps = 1e-7):
        super().__init__()
        self.eps = eps
        
    def forward(self, gt, mask, logit):
        bce = F.binary_cross_entropy_with_logits(logit, gt, reduction = 'none')
        mask_sum = torch.sum(mask, dim = [1, 2]) + self.eps
        return torch.mean(torch.sum(mask * bce, dim = [1, 2]) / mask_sum)

import numpy as np
class IMAGE():
    def __init__(self, model_path):
        device = torch.device('cuda')
        #self.model = SimpleCNN()
        #self.model.load_state_dict(torch.load(model_path, map_location=device))
        self.model = torch.load(model_path, map_location=device)

    def get_binary(self, image):
        """
            将输入图像进行预处理，通过深度学习模型进行预测，并返回二值化结果。
            他喵的，改了半天才发现根本没用到这个函数，我日了狗
        """
        img = np.uint8(np.logical_and(image[:, :, 2] < 240, image[:, :, 2] > 195)) * 128
        cv2.imshow(img, 'binary_img')
        cv2.waitKey(10)
        return img
    

    def get2_binary(self, image):
        """
            将输入图像进行预处理，通过深度学习模型进行预测，并返回二值化结果。
            这里做了一个很难绷的显示操作，没有运行过，所以不知道会不会报错，这里打个标记，以后再改
            注意：在实际使用中，需要保证模型和深度学习库的版本和 CUDA 版本匹配，否则会出现运行时错误。

        """
        cv2.imshow('color_img',image)
        cv2.waitKey(10)
        image = np.float32(image) / 255.0 # 将输入图像转换为浮点数类型，并归一化到 [0, 1] 范围。
        shp = image.shape # 获取图像的形状，存储在 shp 变量中。
        img = torch.from_numpy(image.reshape(1, shp[0], shp[1], shp[2])).to('cuda')# 使用 torch.from_numpy 将 NumPy 数组转换为 PyTorch 张量。
        img = img.permute([0, 3, 1, 2]).contiguous() # 使用 contiguous 方法确保张量在内存中是连续的。
        # 使用 permute 方法调整张量的维度顺序，从 (批量大小, 高度, 宽度, 通道数) 转换为 (批量大小, 通道数, 高度, 宽度)。
        logit = self.model(img) # 使用深度学习模型 self.model 对输入图像进行预测，得到预测结果 logit。
        img = np.uint8((logit[0, 0] > 0.5).cpu().numpy()) * 128
        cv2.imshow('binary_img',img)
        cv2.waitKey(10)

        return img
         # 将预测结果 logit 的第一个元素与 0.5 进行比较，得到二值化结果。
        # 这里有一个从GPU到CPU的转换，因为logit是在GPU上计算的，所以需要将其转移到CPU上才能进行后续操作。
        # 但是，这个转换可能会增加计算时间，因此需要权衡计算速度和内存使用之间的关系。
        # 如果不做这个会发生什么？会发生错误，因为logit是一个在GPU上的张量，不能直接进行NumPy操作。
    