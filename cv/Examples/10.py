import cv2
import numpy as np

image = np.zeros((500,500,3))
cv2.rectangle(image,(50,50),(450,450),(255,0,0),5)
cv2.rectangle(image,(100,100),(400,400),(0,255,0),5)
cv2.rectangle(image,(150,150),(350,350),(0,0,255),5)
cv2.circle(image,(250,250),90,(255,255,255),3)
cv2.line(image,(50,50),(450,450),(255,255,255),5)
cv2.line(image,(50,450),(450,50),(255,255,255),5)
cv2.imshow("Result",image)
cv2.imwrite("Examples/out.png",image)
cv2.waitKey(0)
cv2.destroyAllWindows()