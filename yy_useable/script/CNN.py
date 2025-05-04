from torch import nn
import torch.nn.functional as F
import torch

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
        return np.uint8(np.logical_and(image[:, :, 2] < 240, image[:, :, 2] > 195)) * 128

    def get2_binary(self, image):
        image = np.float32(image) / 255.0
        shp = image.shape
        img = torch.from_numpy(image.reshape(1, shp[0], shp[1], shp[2])).to('cuda')
        img = img.permute([0, 3, 1, 2]).contiguous()
        logit = self.model(img)
        return np.uint8((logit[0, 0] > 0.5).cpu().numpy()) * 128