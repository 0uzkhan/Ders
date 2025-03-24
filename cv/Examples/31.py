import cv2

image1 = cv2.imread("Examples/lena.png")
image1 = cv2.resize(image1, (400, 400))
image2 = cv2.imread("Examples/python.png")
image2 = cv2.resize(image2, (400, 400))

result1 = cv2.add(image1, image2)
result2 = cv2.addWeighted(image1, 0.2, image2, 0.8, gamma=10)
result3 = cv2.subtract(image1, image2)

cv2.imshow("Result 1", result1)
cv2.imshow("Result 2", result2)
cv2.imshow("Result 3", result3)

cv2.waitKey(0)
cv2.destroyAllWindows()