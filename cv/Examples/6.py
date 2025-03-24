import cv2

resim = cv2.imread("Examples/lena.png",0)
cv2.rectangle(resim,(110,10),(350,280),255,3)
cv2.imshow("resim",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()