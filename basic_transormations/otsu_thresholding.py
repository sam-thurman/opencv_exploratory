import cv2
import numpy as np

reduce_noise = False

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        break

    # Read the image in a grayscale mode
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce image noise if it is required
    if reduce_noise:
        frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # Apply Otsu thresholding
    #   'otsu_threshold' will be the current threshold value chosen by the algo
    #   'frame' will be the image with the threshold applied
    otsu_threshold, frame = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU,)

    cv2.imshow('Otsu', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()