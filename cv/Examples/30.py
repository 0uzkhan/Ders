import cv2
import numpy as np

image1 = cv2.imread("Examples/lena.png")
image2 = cv2.imread("Examples/lena.png")

image1 = cv2.resize(image1, (200, 400))
image2 = cv2.resize(image2, (200, 400))

result1 = cv2.hconcat([image1, image2])
result2 = cv2.vconcat([image1, image2])

cv2.imshow("Result 1", result1)
cv2.imshow("Result 2", result2)
cv2.waitKey(0)
cv2.destroyAllWindows()