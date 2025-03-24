import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Examples/lena.png')
fig, ax = plt.subplots(1,2)
ax[0].imshow(image)
ax[1].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()