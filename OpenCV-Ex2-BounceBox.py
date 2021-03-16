import cv2
import numpy as np
import random

img = np.zeros((500, 500, 3), dtype=np.uint8)
xcord1 = 0
xcord2 = 50
ycord1 = 0
ycord2 = 50
thicc = 3
i = 0
color = [255, 255, 255]

while True:
    while xcord2 < 497:
        xcord1 += 1
        xcord2 += 1
        cv2.imshow('img', img)
        img = np.zeros((500, 500, 3), dtype=np.uint8)
        cv2.rectangle(img, (xcord1, ycord1), (xcord2, ycord2), color, thicc)
        cv2.waitKey(5)
        if xcord2 == 497:
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            break
    while ycord2 < 497:
        ycord1 += 1
        ycord2 += 1
        cv2.imshow('img', img)
        img = np.zeros((500, 500, 3), dtype=np.uint8)
        cv2.rectangle(img, (xcord1, ycord1), (xcord2, ycord2), color, thicc)
        cv2.waitKey(5)
        if ycord2 == 497:
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            break
    while xcord1 > 3:
        xcord1 -= 1
        xcord2 -= 1
        cv2.imshow('img', img)
        img = np.zeros((500, 500, 3), dtype=np.uint8)
        cv2.rectangle(img, (xcord1, ycord1), (xcord2, ycord2), color, thicc)
        cv2.waitKey(5)
        if xcord1 == 3:
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            break
    while ycord2 > 3:
        ycord1 -= 1
        ycord2 -= 1
        cv2.imshow('img', img)
        img = np.zeros((500, 500, 3), dtype=np.uint8)
        cv2.rectangle(img, (xcord1, ycord1), (xcord2, ycord2), color, thicc)
        cv2.waitKey(5)
        if ycord1 == 3:
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            break