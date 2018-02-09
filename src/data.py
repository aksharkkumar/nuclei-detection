import os, re, glob
import numpy as np
import imageio

from PIL import Image

class Nuclei(object):
    def __init__(self,dir_path):
        self.dir = os.path.normpath(dir_path)
        self.key = os.path.dirname(dir_path)
        self.image = self.load_nuclei_image()
        self.masks = self.load_nuclei_masks()



    def load_nuclei_image(self):
        img_path = self.dir + 'images/'
        image = imageio.imread(img_path)
        return image    
        
    def load_nuclei_masks(self):
        mask_path = os.path.join(self.dir, 'masks/*.png')
        mask_images = glob.glob(mask_path)
        masks = dict()
        for mask_image in mask_images:
            match = re.search("(.*).png",mask_image)
            mask_key = match.group(1)
            mask = imageio.imread(mask_image)
            masks[mask_key] = mask
        return masks
        