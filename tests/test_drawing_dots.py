import sys
sys.path.append("..")

from tools.drawing import draw_dots

import cv2
result = draw_dots("D:\\github_repo\\simple-cv-demos\\static\\0.png",
                   points=[(200, 200), (300, 300), (400, 400), (500, 500),
                           (600, 600), (700, 700)])

cv2.imwrite("result.jpg", result)
