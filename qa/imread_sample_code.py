sample_code = '''
import cv2
import os

if os.path.exists("some_image.jpg"): # if the file is not exist, won`t raise an exception but image is None
    image = cv2.imread("some_image.jpg") # should be image type
    print(type(image)) # <class 'numpy.ndarray'>

"""
# if the image type is .tif, there maybe some errors with opencv
# actually, using scikit to load an image is better, eg.
"""

from skimage import io
if os.path.exists("some_image.jpg"): # if the file is not exist, it raises an exception
    image = io.imread("some_image.jpg")
    print(type(image)) # <class 'numpy.ndarray'>
'''