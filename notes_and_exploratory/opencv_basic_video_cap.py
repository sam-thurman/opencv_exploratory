import os
import sys
import argparse
import numpy as numpy
import cv2 as cv

# arg for VideoCapture is which camera/src to use for the capture
# 0 will be webcam, could also use -1 if no other cameras are connected
cap = cv.VideoCapture(0)

if not cap.isOpened:
  print('Unable to open camera')

while True:
  # capture frame-by-frame
  ret, frame = cap.read()
  
  # operations on the frame
  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

  # display the resulting frame
  cv.imshow('frame',gray)
  # press "q" to exit
  if cv.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv.destroyAllWindows()