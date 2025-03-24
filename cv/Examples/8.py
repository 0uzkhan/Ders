import cv2

image = cv2.imread("Examples/lena.png")
cv2.line(image, (0, 0), (511, 511), (150, 200, 0), 5)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()