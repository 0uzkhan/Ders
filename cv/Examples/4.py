import cv2

image = cv2.imread("Examples/lena.png",0)
print(image.shape)
print(image)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()