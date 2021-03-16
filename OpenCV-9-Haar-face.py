import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray, 1.03, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, ), (x + w, y + h), (255, 0, 0), 2)
cv2.imshow('Faces Detected', img)
cv2.waitKey(0)