import numpy as np
import cv2
from _types import StrOrArray

from tools.mosiac import img_mosiac
from common.load_img import load_image


def img_mosiac_with_masks(p: StrOrArray,
                          step: int = 2,
                          mask: np.ndarray = np.ones((3, 3))):
    if type(p) == str:
        p = load_image(p)
    _mosiac_img, scale = img_mosiac(p, step=step, returnScale=True)
    if _mosiac_img is not None:
        assert _mosiac_img.shape[0] == mask.shape[0] and _mosiac_img.shape[
            1] == mask.shape[1], "mask must have same size with image"

        imgShape = _mosiac_img.shape

        _mask = np.zeros((imgShape[0], imgShape[1]))
        for i in range(0, scale[0]):
            for j in range(0, scale[1]):
                if np.sum(mask[i * step:(i + 1) * step,
                               j * step:(j + 1) * step]) > 0:
                    _mask[i * step:(i + 1) * step, j * step:(j + 1) * step] = 1

        _reserved_mask = 1 - _mask
        _mask = cv2.merge([_mask, _mask, _mask])

        _reserved_mask = np.array(cv2.merge(
            [_reserved_mask, _reserved_mask, _reserved_mask]),
                                  dtype=np.uint8)
        result = p * _reserved_mask + _mosiac_img * _mask
        return result
    else:
        return None
