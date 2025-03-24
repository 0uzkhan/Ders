# import cv2
# resim = cv2.imread("Data/deniz_yildizi.jpg")
# cv2.circle(resim,(240,160),150,(150,150,255), 5)
# cv2.imshow("resim",resim)
# cv2.waitKey(1)

import cv2

image = cv2.imread("Examples/lena.png")
cv2.circle(image, (240, 160), 150, (150, 150, 100), 5)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()