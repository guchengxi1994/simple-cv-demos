'''
Descripttion: 
version: 
Author: xiaoshuyui
email: guchengxi1994@qq.com
Date: 2022-02-28 19:02:18
LastEditors: xiaoshuyui
LastEditTime: 2022-02-28 19:03:22
'''
import os
import cv2
import numpy as np
from models import FileNotFoundException, CannotLoadImageByOpencvException

def load_image(p:str)-> np.ndarray:
    if not os.path.exists(p):
        raise FileNotFoundException("{} is not exists".format(p))

    img = cv2.imread(p)

    if img is None:
        raise CannotLoadImageByOpencvException(
            "Cannot load image,check it first".format(p))
    
    assert type(img) is np.ndarray,"type error"

    return img