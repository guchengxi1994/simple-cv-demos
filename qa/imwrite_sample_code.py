sample_code = """
# using cv2

import cv2
import os 

if os.path.exists("some_image.jpg"):
    image = cv2.imread("some_image.jpg")
    cv2.imwrite("other_image_name.jpg",image)

# using skimage

from skimage import io
import os

if os.path.exists("some_image.jpg"):
    image = io.imread("some_image.jpg")
    io.imsave("other_image_name.jpg",image)

"""
