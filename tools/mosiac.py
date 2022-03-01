'''
Descripttion: 
version: 
Author: xiaoshuyui
email: guchengxi1994@qq.com
Date: 2022-02-28 19:00:56
LastEditors: xiaoshuyui
LastEditTime: 2022-02-28 19:04:11
'''
import cv2
import numpy as np
from _types import StrOrArray
from common.load_img import load_image


def img_mosiac(p: StrOrArray,
               step: int = 2,
               begin=(0, 0),
               end=(np.Inf, np.Inf)):
    """see: $projectDir/docs/mosiac.md
    """
    if type(p) == np.ndarray:
        img = p
    else:
        img = load_image(p)

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
