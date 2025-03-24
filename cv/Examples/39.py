import cv2
import numpy as np

image = cv2.imread("Examples/lena.png")
image = cv2.resize(image, (200, 200))
b, g, r = cv2.split(image)

blue = cv2.merge([r, g, b])
green = cv2.merge([b, r, g])
red = cv2.merge([g, b, r])

cv2.imshow("Original", image)
cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Red", red)

cv2.waitKey(0)
cv2.destroyAllWindows()