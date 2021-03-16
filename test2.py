import cv2, random
import numpy as np



xaxis = 500
yaxis = 500
dx = 1
dy = 1
size = 80
thicc = 3
color = [255, 255, 255]
xcord1 = random.randint(0, yaxis - size)
ycord1 = xcord1
xcord2 = xcord1 + size
ycord2 = ycord1 + size


img = np.zeros((xaxis, yaxis, 3), dtype=np.uint8)

def portal():
    global xcord1, xcord2, ycord1, ycord2, color, dx
    cv2.rectangle(img, (xcord1, ycord1), (xcord2, ycord2), color, thicc)
    xcord1 = xcord1 + dx
    xcord2 = xcord2 + dx
    if xcord1 >= xaxis + thicc or xcord1 <= 0 - size - thicc:
        dx = dx * (-1)
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        ycord1 = random.randint(0, yaxis)
        ycord2 = ycord1 + size
    cv2.imshow('Frame', img)
    return

while True:
    img = np.zeros((500, 500, 3), dtype=np.uint8)

    portal()

    if cv2.waitKey(1) & 0xff == ord('q'):
        break



