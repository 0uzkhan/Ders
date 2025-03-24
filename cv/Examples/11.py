import cv2

image = cv2.imread("Examples/lena.png")
cv2.rectangle(image, (150, 100), (400, 250), (0, 0, 255), 5)
image2 = image[200:350, 200:350]
cv2.imshow("image", image)
cv2.imshow("image2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows()