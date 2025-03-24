import cv2
import numpy as np

image = cv2.imread("Examples/lena.png")
cv2.imshow("image1", np.flip(image, 0))
cv2.imshow("image2", np.flip(image, 1))
cv2.imshow("image3", np.flip(image, 2))
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()