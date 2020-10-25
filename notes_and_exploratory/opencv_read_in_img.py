import os
import sys
import numpy as np
import cv2 as cv

### OPENING AN IMAGE
# IMREAD_COLOR loads the image in the BGR 8-bit format. This is the default that is used here.
# IMREAD_UNCHANGED loads the image as is (including the alpha channel if present)
# IMREAD_GRAYSCALE loads the image as an intensity one

try:
    img = cv.imread(cv.samples.findFile("starry_night.jpg"))
except:
    sys.exit("Could not read the image.")

# show image using cv2.imshow
# first argument is the title of the window 
# second argument is the cv::Mat object that will be shown.
cv.imshow("Display window", img)
k = cv.waitKey(0)

# if "s" key is pressed, write image to file "starry_night.png"
if k == ord("s"):
    cv.imwrite("starry_night.png", img)