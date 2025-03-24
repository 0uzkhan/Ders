import cv2
import numpy as np

image = cv2.imread("Examples/lena.png")
cv2.imshow("Original", image)
frame = np.zeros((512, 512, 3), np.uint8)
frame[192:320, 192:320] = [255, 255, 255]
cv2.imshow("Frame", frame)
bool_frame = frame.astype('bool')
frame[bool_frame] = image[bool_frame]
cv2.imshow("Final Image", frame)
cv2.waitKey(0)
cv2.destroyAllWindows
