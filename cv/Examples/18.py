import cv2
import numpy as np

gray = cv2.imread("Examples/lena.png",0)
blackWhite = np.copy(gray)
threshold = np.mean(gray)
blackWhite[blackWhite < threshold] = 0
blackWhite[blackWhite >= threshold] = 255
cv2.imshow("gray",gray)
cv2.imshow("blackWhite",blackWhite)
cv2.waitKey(0)
cv2.destroyAllWindows()