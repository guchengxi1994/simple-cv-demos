from tools.mosiac import img_mosiac
import cv2

result = img_mosiac("D:\\github_repo\\simple-cv-demos\\static\\0.png",step=20,begin=(200,200),end=(400,400))

cv2.imwrite("result.jpg",result)

# result = img_mosiac("D:\\github_repo\\simple-cv-demos\\static\\1.png",step=20)