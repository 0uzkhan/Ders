import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Examples/OpenCV.png',0)
edges1 = cv2.Canny(image,100,200)
edges2 = cv2.Canny(image,50,100)
median = np.median(image)
lowTH = int(max(0, 0.7*median))
highTH = int(max(255, 1.3*median))
edges3 = cv2.Canny(image, lowTH, highTH, L2gradient=True)

fig,ax = plt.subplots(1, 3, figsize=(15,15))
ax[0].set_title("Canny Edge Detection 100-200")
ax[0].imshow(edges1,cmap='gray')
ax[1].set_title("Canny Edge Detection 50-100")
ax[1].imshow(edges2,cmap='gray')
ax[2].set_title("Canny Edge Detection Median")
ax[2].imshow(edges3,cmap='gray')

plt.show()