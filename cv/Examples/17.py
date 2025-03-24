import cv2
import numpy as np

gray = cv2.imread("Examples/lena.png",0)
black_white = np.copy(gray)
black_white[black_white < 128] = 0
black_white[black_white >= 128] = 255
cv2.imshow("gray",gray)
cv2.imshow("black_white",black_white)
cv2.waitKey(0)
cv2.destroyAllWindows()