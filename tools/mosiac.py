import numpy as np
import cv2
import os
from models import FileNotFoundException, CannotLoadImageByOpencvException


def img_mosiac(p: str, step: int = 2, begin=(0, 0), end=(np.Inf, np.Inf)):
    """doc can be found in ../docs/mosiac.md

    """
    if not os.path.exists(p):
        print("pppppp")
        raise FileNotFoundException("{} is not exists".format(p))

    img = cv2.imread(p)

    if img is None:
        raise CannotLoadImageByOpencvException(
            "Cannot load image,check it first".format(p))

    assert begin[0] < end[0] and begin[1] < end[1], "param error"

    imgShape = img.shape
    if len(imgShape) == 3:
        imgList = cv2.split(img)
    else:
        imgList = [img, img, img]

    startX = 0
    startY = 0
    endX = imgShape[0]
    endY = imgShape[1]

    if end[0] <= endX:
        endX = end[0]

    if begin[0] >= startX:
        startX = begin[0]

    if end[1] <= endY:
        endY = end[1]

    if begin[1] >= startY:
        startY = begin[1]

    for i in imgList:
        for r in range(startX, endX, step):
            for c in range(startY, endY, step):
                _mean = np.mean(i[r:r + step, c:c + step])
                i[r:r + step, c:c + step] = _mean

    result = cv2.merge(imgList)
    return result
