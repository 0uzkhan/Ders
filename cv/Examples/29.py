import cv2
import numpy as np

image = cv2.imread("Examples/lena.png",0)
image_new = image.copy()
gamma = 1.1
image_new = np.power(image_new, gamma)
image_new = np.clip(image_new,0,255)
image_new = np.uint8(image_new)

cv2.imshow("Original",image)
cv2.imshow("Resut",image_new)
cv2.waitKey(0)
cv2.destroyAllWindows()