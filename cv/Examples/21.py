import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Examples/lena.png")
image = cv2.resize(image, (400, 400))
imageAnd = np.zeros((400, 400, 3), dtype=np.uint8)
cv2.circle(imageAnd, (200, 200), 150, (255, 255, 255), -1)

rectangle = np.zeros((400, 400, 3), dtype=np.uint8)
cv2.rectangle(rectangle, (75, 75), (325, 325), (255, 255, 255), -1)

circle = np.zeros((400, 400, 3), dtype=np.uint8)
cv2.circle(circle, (200, 200), 150, (255, 255, 255), -1)

notImage = cv2.bitwise_not(rectangle)
andImage = cv2.bitwise_and(rectangle, circle)
orImage = cv2.bitwise_or(rectangle, circle)
xorImage = cv2.bitwise_xor(rectangle, circle)
imageAnded = cv2.bitwise_and(image, imageAnd)

plt.figure(figsize=(10, 10))
plt.subplot(3, 3, 1)
plt.imshow(cv2.cvtColor(rectangle, cv2.COLOR_BGR2RGB))
plt.title("Rectangle")

plt.subplot(3, 3, 2)
plt.imshow(cv2.cvtColor(circle, cv2.COLOR_BGR2RGB))
plt.title("Circle")

plt.subplot(3, 3, 3)
plt.imshow(cv2.cvtColor(notImage, cv2.COLOR_BGR2RGB))
plt.title("Not")

plt.subplot(3, 3, 4)
plt.imshow(cv2.cvtColor(andImage, cv2.COLOR_BGR2RGB))
plt.title("And")

plt.subplot(3, 3, 5)
plt.imshow(cv2.cvtColor(orImage, cv2.COLOR_BGR2RGB))
plt.title("Or")

plt.subplot(3, 3, 6)
plt.imshow(cv2.cvtColor(xorImage, cv2.COLOR_BGR2RGB))
plt.title("Xor")

plt.subplot(3, 3, 7)
plt.imshow(cv2.cvtColor(imageAnded, cv2.COLOR_BGR2RGB))
plt.title("Image Anded")

plt.show()
