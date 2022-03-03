import cv2
import numpy as np
from _types import StrOrArray, IntOrTuple
from common.load_img import load_image
from decorators import CvToolDecorator


@CvToolDecorator.checkParam("kernelSize",
                            paramTypeList=IntOrTuple.__constraints__)
def blur(p: StrOrArray,
         kernelSize: IntOrTuple,
         borderType: str = "constant") -> np.ndarray:
    """if param kernelSize is an integer, then generate _kernel with np.ones((kernelSize,kernelSize))/(kernelSize*kernelSize),\n
       if param kernelSize is a tuple, then generate _kernel with np.ones(kernelSize)/(kernelSize[0]*kernelSize[1]),\n
       
       This result is equals filter2D function under some conditions,try
       --------
       >>> dst = filter2D(image_path,kernel=np.ones((15,15))/(15*15))
       >>> dst2 = blur(image_path,kernelSize=(15,15))
       >>> c = (dst==dst2)
       >>> print(c.all())
       
       True
    """
    if type(p) == np.ndarray:
        img = p
    else:
        img = load_image(p)

    if type(kernelSize) == int:
        _kernel = (kernelSize, kernelSize)
    else:
        assert len(kernelSize) == 2 and int(kernelSize[0]) != 0 and int(
            kernelSize[1]) != 0, "input error"
        _kernel = kernelSize

    if borderType == "constant":
        _borderType = cv2.BORDER_CONSTANT
    else:
        _borderType = cv2.BORDER_DEFAULT

    dst = cv2.blur(img, _kernel, borderType=_borderType)
    return dst