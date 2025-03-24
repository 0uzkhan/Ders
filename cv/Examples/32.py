import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Examples/lena.png',0)
ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
thresh3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,
cv2.THRESH_BINARY,11,2)
thresh4 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
cv2.THRESH_BINARY,11,2)

fig,ax = plt.subplots(2, 3, figsize=(10,10))
ax[0,0].set_title("Orginal Image")
ax[0,0].imshow(image,cmap='gray')
ax[0,1].set_title("Global Thresholding (v=127)")
ax[0,1].imshow(thresh1,cmap='gray')
ax[0,2].set_title("Otsu's Thresholding")
ax[0,2].imshow(thresh2,cmap='gray')
ax[1,0].set_title("Adaptive Mean Thresholding")
ax[1,0].imshow(thresh3,cmap='gray')
ax[1,1].set_title("Adaptive Gaussian Thresholding")
ax[1,1].imshow(thresh4,cmap='gray')

plt.show()