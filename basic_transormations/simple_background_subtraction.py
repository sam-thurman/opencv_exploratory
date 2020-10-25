import cv2 as cv
import argparse

parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              OpenCV. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')

args = parser.parse_args()

if args.algo == 'MOG2':
    backSub = cv.createBackgroundSubtractorMOG2()
else:
    backSub = cv.createBackgroundSubtractorKNN()

thresh_val = 127
thresh_maxVal = 255

cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        break
  
    # # to-zero thresholding
    # ret, thresh = cv.threshold(frame,thresh_val,thresh_maxVal,cv.THRESH_TOZERO)
  
    # adaptive thresholding
    ad_thresh = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    # apply background subtraction mask
    fgMask = backSub.apply(add_thresh, learningRate=0.5)
    
    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(frame, str(cap.get(cv.CAP_PROP_POS_FRAMES)), (15, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    
    cv.imshow('Frame', frame)
    cv.imshow('FG Mask', fgMask)
    # cv.imshow('W/ Thresholding', thresh)
  
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()