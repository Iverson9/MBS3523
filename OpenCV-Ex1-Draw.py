import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype=np.uint8)
cv2.rectangle(img, (0, 500), (500, 0), (20, 255, 0), -1)
cv2.rectangle(img, (125, 125), (375, 375), (255, 0, 255), 3)
cv2.circle(img, (125, 125), 30, (0, 51, 102), 2)
cv2.circle(img, (125, 375), 30, (0, 51, 102), 2)
cv2.circle(img, (375, 125), 30, (0, 51, 102), 2)
cv2.circle(img, (375, 375), 30, (0, 51, 102), 2)
cv2.line(img, (250, 0), (250, 500), (0, 0, 255), 5)
cv2.line(img, (0, 250), (500, 250), (0, 0, 255), 5)
cv2.imshow('img', img)
cv2.waitKey(0)