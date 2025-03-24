import cv2
image = cv2.imread("Examples/lena.png")
cv2.rectangle(image,(110,10),(350,280),(255,0,0),3)
cv2.imshow("resim",image)
cv2.waitKey(0)
cv2.destroyAllWindows()