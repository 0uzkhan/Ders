import cv2
import numpy as np

image = cv2.imread("Examples/lena.png")
res9 = cv2.medianBlur(image,9)

cv2.imshow("Original",image)
cv2.imshow("Resut",res9)
cv2.waitKey(0)
cv2.destroyAllWindows()