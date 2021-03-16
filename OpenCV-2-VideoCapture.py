import cv2
import numpy as np

capture = cv2.VideoCapture('Resources/dog.mp4')
while True:
    success, img = capture.read()
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (int(img.shape[1] / 1.5), int(img.shape[0] / 1.5)))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame', img)
    cv2.imshow('Gray Image', imgGray)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()