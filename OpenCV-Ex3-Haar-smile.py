import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('Resources/haarcascade_smile.xml')
eyeCascade = cv2.CascadeClassifier('Resources/haarcascade_eye.xml')

capture = cv2.VideoCapture('Resources/ricardo.mp4')
#capture = cv2.VideoCapture(0)
capture.set(3, 1920)
capture.set(4, 1080)

while True:
    success, img = capture.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.05, 3)
    smiles = smileCascade.detectMultiScale(imgGray, 1.3, 25)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(img, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)
        cv2.putText(img, 'Smile', (sx, sy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Frame', img)
    cv2.moveWindow('Frame', 100, 20)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()