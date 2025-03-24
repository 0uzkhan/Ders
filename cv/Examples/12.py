import cv2
import numpy as np

image = cv2.imread("Examples/lena.png")
source = cv2.imread("Examples/lena.png")
cv2.rectangle(source, (100, 100), (200, 200), (0, 0, 255), 5)
part = source[100:200, 100:200]
newImage = np.copy(image)
newImage[300:400, 100:200] = part
cv2.imshow("image", image)
cv2.imshow("source", source)
cv2.imshow("part", part)
cv2.imshow("newImage", newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()