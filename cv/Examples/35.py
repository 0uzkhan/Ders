import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('Examples/OpenCV.png',0)

PrewitKernelX = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
PrewitKernelY = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
PrewitX = cv2.filter2D(image, cv2.CV_64F, PrewitKernelX)
PrewitY = cv2.filter2D(image, cv2.CV_64F, PrewitKernelY)
Prewit = np.sqrt(PrewitX**2 + PrewitY**2)
Prewit = np.uint8(Prewit)

RobertsKernelX = np.array([[1,0],[0,-1]])
RobertsKernelY = np.array([[0,1],[-1,0]])
RobertsX = cv2.filter2D(image, cv2.CV_64F, RobertsKernelX)
RobertsY = cv2.filter2D(image, cv2.CV_64F, RobertsKernelY)
Roberts = np.sqrt(RobertsX**2 + RobertsY**2)
Roberts = np.uint8(Roberts)

fig,ax = plt.subplots(2, 3, figsize=(15,15))

ax[0,0].set_title("Prewit X")
ax[0,0].imshow(PrewitX,cmap='gray')
ax[0,1].set_title("Prewit Y")
ax[0,1].imshow(PrewitY,cmap='gray')
ax[0,2].set_title("Prewit X + Y")
ax[0,2].imshow(Prewit,cmap='gray')

ax[1,0].set_title("Roberts X")
ax[1,0].imshow(RobertsX,cmap='gray')
ax[1,1].set_title("Roberts Y")
ax[1,1].imshow(RobertsY,cmap='gray')
ax[1,2].set_title("Roberts X + Y")
ax[1,2].imshow(Roberts,cmap='gray')

plt.show()