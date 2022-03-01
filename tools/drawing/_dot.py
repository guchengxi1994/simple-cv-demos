from typing import List

import cv2
import numpy as np
from _types import StrOrArray
from common.load_img import load_image


def draw_dots(p: StrOrArray,
              points: List[tuple],
              color: tuple = (0, 0, 255),
              thickness: int = 4,
              pointSize: int = 1):
    """see: $projectDir/docs/drawing.md
    """
    if type(p) == np.ndarray:
        img = p
    else:
        img = load_image(p)

    for i in points:
        img = __draw_single_dot(img, i, color, thickness, pointSize)

    return img


def __draw_single_dot(p: StrOrArray,
                      point: tuple,
                      color: tuple = (0, 0, 255),
                      thickness: int = 4,
                      pointSize: int = 1) -> np.ndarray:
    if type(p) == np.ndarray:
        img = p
    else:
        img = load_image(p)

    if point[0] <= img.shape[0] and point[1] <= img.shape[1]:
        cv2.circle(img, point, pointSize, color, thickness)

    return img
