import sys

sys.path.append("..")
import numpy as np
import cv2
from tools.conv import filter2D,blur

# dst = filter2D("D:\\github_repo\\simple-cv-demos\\static\\0.png",kernel=np.ones((15,15))/(15*15))
dst = filter2D("D:\\github_repo\\simple-cv-demos\\static\\0.png",kernel=(15,15))

# cv2.imwrite("result.jpg",dst)
dst2 = blur("D:\\github_repo\\simple-cv-demos\\static\\0.png",kernelSize=(15,15))

c = (dst==dst2)

print(c.all())