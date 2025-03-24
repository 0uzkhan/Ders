import cv2
import numpy as np

image = cv2.imread("Examples/OpenCV.png")
image = cv2.resize(image, (300, 300))
kernel = np.ones((15,15),np.uint8)
erosion = cv2.erode(image,kernel)
dilation = cv2.dilate(image,kernel)
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original",image)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilation)
cv2.imshow("Opening",opening)
cv2.imshow("Closing",closing)

cv2.waitKey(0)
cv2.destroyAllWindows()