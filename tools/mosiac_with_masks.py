import cv2
import numpy as np
from _types import StrOrArray

from tools.mosiac import img_mosiac


def img_mosiac_with_masks(p: StrOrArray,
                          step: int = 2,
                          begin=(0, 0),
                          mask: np.ndarray = np.ones((3, 3))):
    _mosiac_img = img_mosiac(p, step=step)
    if _mosiac_img is not None:
        assert _mosiac_img.shape[0] == mask.shape[0] and _mosiac_img.shape[
            1] == mask.shape[1], "mask must have same size with image"

        