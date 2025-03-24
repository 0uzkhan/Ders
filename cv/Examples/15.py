import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1 = np.ones([250,250]) * 255
img2 = np.ones([250,250]) * 128
img3 = np.ones([250,250]) * 0
fig, ax = plt.subplots(3,1)
ax[0].imshow(img1,'gray',vmin=0,vmax=255)
ax[1].imshow(img2,'gray',vmin=0,vmax=255)
ax[2].imshow(img3,'gray',vmin=0,vmax=255)
plt.show()