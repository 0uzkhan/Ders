import cv2
import numpy as np

image = cv2.imread("Examples/lena.png")
image = cv2.resize(image, (400, 400))
image1 = image[0:200, 0:200]
image2 = image[0:200, 200:400]
image3 = image[200:400, 0:200]
image4 = image[200:400, 200:400]

newImage = np.zeros((400, 400, 3), np.uint8)
newImage[0:200, 0:200] = image4
newImage[0:200, 200:400] = image3
newImage[200:400, 0:200] = image2
newImage[200:400, 200:400] = image1

cv2.imshow("Original", image)
cv2.imshow("Result", newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()