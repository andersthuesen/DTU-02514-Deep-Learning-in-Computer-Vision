import os
import torch
import numpy as np
import glob
import PIL.Image as Image
import gdown

class SVHNBackgroundImages(torch.utils.data.Dataset):
    def __init__(self, train, transform, data_path='SVHN/SVHN/background'):
        self.transform = transform
        data_path = os.path.join(data_path, 'train' if train else 'test')
        self.image_paths = glob.glob(data_path + '/*.png')
        
    def __len__(self):
        'Returns the total number of samples'
        return len(self.image_paths)

    def __getitem__(self, idx):
        'Generates one sample of data'
        image_path = self.image_paths[idx]
        
        image = Image.open(image_path)
        X = self.transform(image)
        return X, 10 # Always return class 10, since all are background images