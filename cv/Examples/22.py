import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('Examples/lena.png',0)
histogram = cv2.calcHist([image],channels=[0],mask=None,histSize=[256],ranges=[0,256])
fig, ax = plt.subplots(1,2,figsize=(10,5))
ax[0].imshow(image,cmap='gray')
ax[0].axis('off')
ax[1].plot(histogram)
plt.show()
