import cv2
import matplotlib.pyplot as plt

image = cv2.imread("Examples/lena.png")
res3 = cv2.GaussianBlur(image,(3,3),0)
res5 = cv2.GaussianBlur(image,(5,5),0)
res9 = cv2.GaussianBlur(image,(9,9),0)
res25 = cv2.GaussianBlur(image,(25,25),0)

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.imshow(cv2.cvtColor(res3, cv2.COLOR_BGR2RGB))
plt.title("3x3")

plt.subplot(2,2,2)
plt.imshow(cv2.cvtColor(res5, cv2.COLOR_BGR2RGB))
plt.title("5x5")

plt.subplot(2,2,3)
plt.imshow(cv2.cvtColor(res9, cv2.COLOR_BGR2RGB))
plt.title("9x9")

plt.subplot(2,2,4)
plt.imshow(cv2.cvtColor(res25, cv2.COLOR_BGR2RGB))
plt.title("25x25")

plt.show()