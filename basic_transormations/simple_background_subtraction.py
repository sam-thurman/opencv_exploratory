import cv2
import argparse

parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
                                              Opencv2. You can process both videos and images.')
parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='KNN')

args = parser.parse_args()

if args.algo == 'MOG2':
    backSub = cv2.createBackgroundSubtractorMOG2()
else:
    backSub = cv2.createBackgroundSubtractorKNN()

thresh_val = 127
thresh_maxVal = 255

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        break
    
    # convert to gray
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     # apply background subtraction mask
    frame = backSub.apply(frame, learningRate=0.2)

    # # to-zero thresholding
    # ret, thresh = cv2.threshold(frame,thresh_val,thresh_maxVal,cv2.THRESH_TOZERO)

    # # adaptive thresholding
    # ad_thresh = cv2.adaptiveThreshold(grayFrame,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    
    # Otsu thresholding
    otsu_threshold, frame = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)


   
    
    cv2.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv2.putText(frame, str(cap.get(cv2.CAP_PROP_POS_FRAMES)), (15, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    
    cv2.imshow('Frame', frame)
    # cv2.imshow('W/ Thresholding', thresh)
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()