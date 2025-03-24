import cv2
import numpy as np

image = cv2.imread("Examples/lena.png",0)
kernel=np.array([
[1,1,1],
[1,1,1],
[1,1,1]]) / 9
res = cv2.filter2D(image,-1,kernel)
cv2.imshow("Original",image)
cv2.imshow("Resut",res)
cv2.waitKey(0)
cv2.destroyAllWindows()