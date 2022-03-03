import cv2
import numpy as np
from _types import StrOrArray, IntOrTupleOrArray
from common.load_img import load_image
from decorators import CvToolDecorator


@CvToolDecorator.checkParam("kernel",
                            paramTypeList=IntOrTupleOrArray.__constraints__)
def filter2D(p: StrOrArray,
             kernel: IntOrTupleOrArray,
             borderType: str = "constant") -> np.ndarray:
    """ if param kernel is an integer, then generate _kernel with np.ones((kernel,kernel))/(kernel*kernel),\n
        if param kernel is a tuple, then generate _kernel with np.ones(kernel)/(kernel[0]*kernel[1]),\n
        if param kernel is a np.ndarray, then _kernel = kernel.\n
    """
    if type(p) == np.ndarray:
        img = p
    else:
        img = load_image(p)

    if type(kernel) == int:
        _kernel = np.ones((kernel, kernel)) / (kernel * kernel)
    elif type(kernel) == tuple:
        assert len(kernel) == 2 and int(kernel[0]) != 0 and int(
            kernel[1]) != 0, "input error"
        _kernel = np.ones(kernel) / (kernel[0] * kernel[1])
    else:
        _kernel = kernel

    if borderType == "constant":
        _borderType = cv2.BORDER_CONSTANT
    else:
        _borderType = cv2.BORDER_DEFAULT

    dst = cv2.filter2D(img, -1, _kernel, borderType=_borderType)
    return dst