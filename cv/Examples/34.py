import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Examples/OpenCV.png',0)
edges1 = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
edges2 = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)
edges3 = np.sqrt(edges1**2 + edges2**2)

fig,ax = plt.subplots(1, 3, figsize=(15,15))
ax[0].set_title("Sobel X")
ax[0].imshow(edges1,cmap='gray')
ax[1].set_title("Sobel Y")
ax[1].imshow(edges2,cmap='gray')
ax[2].set_title("Sobel X + Sobel Y")
ax[2].imshow(edges3,cmap='gray')

plt.show()