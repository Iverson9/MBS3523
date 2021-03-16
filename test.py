import cv2, random
import numpy as np

xaxis = 640
yaxis = 480
capture = cv2.VideoCapture(0)
capture.set(3, xaxis) # 3 is the width of the frame
capture.set(4, yaxis) # 4 is the height of the frame


dx = 1
dy = 1
size = 80
thicc = 3
color = [255, 255, 255]
xcord1 = random.randint(0, yaxis - size)
ycord1 = xcord1
xcord2 = xcord1 + size
ycord2 = ycord1 + size

while True:
    success, img = capture.read()

    cv2.rectangle(img, (xcord1, ycord1), (xcord2, ycord2), color, thicc)
    xcord1 = xcord1 + dx
    xcord2 = xcord2 + dx
    #ycord1 = xcord1 + dy
    #ycord2 = xcord2 + dy
    if xcord1 >= xaxis + thicc or xcord1 <= 0 - size - thicc:
        dx = dx * (-1)
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        ycord1 = random.randint(0, yaxis)
        ycord2 = ycord1 + size
    cv2.imshow('Frame', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()
