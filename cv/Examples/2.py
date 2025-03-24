import cv2

image = cv2.imread("Examples/lena.png")
cv2.imshow("Lena", image)
cv2.waitKey(0)
cv2.destroyAllWindows()