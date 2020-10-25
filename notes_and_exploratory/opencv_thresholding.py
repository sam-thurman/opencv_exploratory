### cv2.threshold
# If pixel value is greater than a threshold value, 
#     it is assigned one value (may be white), 
#     else it is assigned another value (may be black). 

# First argument: the source image, should be a grayscale image. 
# Second argument: the threshold value which is used to classify the pixel values. 
# Third argument: the maxVal which represents the value to be given if pixel value is 
#     more than (sometimes less than) the threshold value. 
# Fourth argument: different options provided by OpenCV for the type of thresholding
#     cv2.THRESH_BINARY
#     cv2.THRESH_BINARY_INV
#     cv2.THRESH_TRUNC
#     cv2.THRESH_TOZER
#     cv2.THRESH_TOZERO_INV

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../imgs/linear_gradient.png', 0)

# higher values remove lighter pixels
thresh_val = 127
# value of thresholded values will be black
maxVal = 255

ret,thresh1 = cv2.threshold(img,thresh_val,maxVal,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,thresh_val,maxVal,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,thresh_val,maxVal,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,thresh_val,maxVal,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,thresh_val,maxVal,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(np.asarray(images[i]),'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

