import os
import torch
import numpy as np
import glob
import PIL.Image as Image


class horse2zebra(torch.utils.data.Dataset):
    def __init__(self, transform, train=True, data_path='horse2zebra/'):
        'Initialization'
        mode = 'train'
        if not train:
            mode = 'test'
        self.transform = transform
        data_path = os.path.join(data_path, mode)
        self.horse_paths = glob.glob(data_path + '/A/*.jpg')
        self.zebra_paths = glob.glob(data_path + '/B/*.jpg')

    def __len__(self):
        'Returns the total number of samples'
        return len(self.zebra_paths)

    def __getitem__(self, idx):
        'Generates one sample of data'
        
        horse_path = self.horse_paths[idx % len(self.horse_paths)]
        zebra_path = self.zebra_paths[idx % len(self.zebra_paths)]
        
        horse = Image.open(horse_path).convert('RGB')
        zebra = Image.open(zebra_path).convert('RGB')

        horse = self.transform(horse)
        zebra = self.transform(zebra)

        horse = 2 * (horse / torch.max(horse)) - 1
        zebra = 2 * (zebra / torch.max(zebra)) - 1
       
        return horse, zebra

