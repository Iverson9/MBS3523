import cv2

img = cv2.imread('Resources/lena.png')
img = cv2.resize(img, (int(img.shape[1]/1.5), int(img.shape[0]/1.5)))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Lena', img)
cv2.imshow('Gray Image', imgGray)
cv2.waitKey(0)