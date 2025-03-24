import cv2
import numpy as np
import matplotlib.pyplot as plt

image = np.array([
[0, 0, 1, 1, 0, 0],
[0, 0, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 1],
[0, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 0],
[1, 1, 0, 1, 1, 0]
], dtype=np.uint8)

num_labels, labels = cv2.connectedComponents(image)
print(num_labels - 1)

plt.imshow(labels, cmap="nipy_spectral")
plt.title("Connected Components")
plt.show()