import cv2

image = cv2.imread("Examples/lena.png")
cv2.putText(image, "Lena", (40, 150), 2, 2, (255, 0, 0))
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()