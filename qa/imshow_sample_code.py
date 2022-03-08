sample_code = '''
# using cv2

import cv2
image = cv2.imread("some_image.jpg")
cv2.imshow("image",image)
cv2.waitKey(0)

# using skimage

from skimage import io
image = io.imread("some_image.jpg")
io.imshow(image)
io.show()

# also, you can display an image with skimage even if it was loaded by cv2

from skimage import io
import cv2

image = cv2.imread("some_image.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) # this is necessary, because images loaded by cv2 are "RGB" but loaded by skimage are "RGB"

io.imshow(image)
io.show()

# and this is supported too

from skimage import io
import cv2

image = io.imread("some_image.jpg")
image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR) # this is necessary, because images loaded by cv2 are "RGB" but loaded by skimage are "RGB"

cv2.imshow("image",image)
cv2.waitKey(0)

'''