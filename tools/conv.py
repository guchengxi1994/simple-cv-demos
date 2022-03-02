import cv2
import numpy as np
from _types import StrOrArray
from common.load_img import load_image


def filter2D(p: StrOrArray, kernel: np.ndarray):
    if type(p) == np.ndarray:
        img = p
    else:
        img = load_image(p)

    dst = cv2.filter2D(img,-1,kernel,borderType=cv2.BORDER_CONSTANT)
    # dst = cv2.blur(img,(15,15))
    return dst