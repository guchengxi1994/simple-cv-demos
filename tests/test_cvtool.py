import sys
sys.path.append("..")

import cv2
from cvtool import CvTool

cvtool = CvTool("D:\\github_repo\\simple-cv-demos\\static\\0.png")

cvtool.then("mosiac",step=25)

cvtool.showDoc("mosiac")

cv2.imwrite("result.jpg",cvtool.image)