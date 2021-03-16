import numpy as np
import cv2, random

xaxis = 500
yaxis = 500
size = 80
thicc = 3
color = [255, 255, 255]
xcord1 = random.randint(0, yaxis - size)
ycord1 = xcord1
xcord2 = xcord1 + size
ycord2 = xcord2



img = np.zeros((xaxis, yaxis, 3), dtype=np.uint8)

cv2.rectangle(img, (xcord1, ycord1), (xcord2, ycord2), color, thicc)
cv2.putText(img, 'x1y1', (xcord1, ycord1),  cv2.FONT_HERSHEY_SIMPLEX,  0.5, (0, 0, 255), 1, cv2.LINE_AA)
cv2.putText(img, 'x2y2', (xcord2, ycord2),  cv2.FONT_HERSHEY_SIMPLEX,  0.5, (0, 0, 255), 1, cv2.LINE_AA)
cv2.putText(img, 'x1y2', (xcord1, ycord2),  cv2.FONT_HERSHEY_SIMPLEX,  0.5, (0, 0, 255), 1, cv2.LINE_AA)
cv2.putText(img, 'x2y1', (xcord2, ycord1),  cv2.FONT_HERSHEY_SIMPLEX,  0.5, (0, 0, 255), 1, cv2.LINE_AA)
cv2.imshow('img', img)
cv2.waitKey(0)