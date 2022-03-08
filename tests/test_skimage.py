from skimage import io
import cv2

image = cv2.imread("D:\\github_repo\\simple-cv-demos\\static\\0.png")
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

io.imshow(image)
io.show()