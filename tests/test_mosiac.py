import sys

import numpy as np
sys.path.append("..")

from tools.mosiac import img_mosiac
from tools.mosiac_with_masks import img_mosiac_with_masks
import cv2

# result = img_mosiac("D:\\github_repo\\simple-cv-demos\\static\\0.png",step=20,)

# result = img_mosiac("D:\\github_repo\\simple-cv-demos\\static\\0.png",step=20,begin=(200,200),end=(400,400))

# cv2.imwrite("result.jpg",result)

# result = img_mosiac("D:\\github_repo\\simple-cv-demos\\static\\1.png",step=20)

mask = np.zeros((1024,1024))

mask[50:400,700:800] = 1

result2 = img_mosiac_with_masks("D:\\github_repo\\simple-cv-demos\\static\\0.png",step=20,mask=mask)

cv2.imwrite("result.jpg",result2)