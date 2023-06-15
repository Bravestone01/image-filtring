1. Import the necessary packages:

python
import cv2
import numpy as np
from matplotlib import pyplot as plt


2. Read the image:

python
img = cv2.imread('image.png',0)


3. Apply the Gaussian filter:

python
blur = cv2.GaussianBlur(img,(5,5),0)


The second argument (5,5) defines the kernel size of the filter, which can be adjusted depending on the desired effect. The third argument (0) specifies the standard deviation of the Gaussian distribution.

4. Display the original and the blurred image:

python
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur,cmap = 'gray')
plt.title('Blurred Image'), plt.xticks([]), plt.yticks([])
plt.show()