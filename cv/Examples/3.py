import cv2

image = cv2.imread("Examples/lena.png")
blue = image[:,:,0]
green = image[:,:,1]
red = image[:,:,2]

cv2.imshow("Blue", blue)
cv2.imshow("Green", green)
cv2.imshow("Red", red)
cv2.waitKey(0)
cv2.destroyAllWindows()