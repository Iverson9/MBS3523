import cv2, random

xaxis = 640
yaxis = 480
capture = cv2.VideoCapture(0)
capture.set(3, xaxis)
capture.set(4, yaxis)
dx = -1
dy = -1
size = 80
thicc = 3
color = [255, 255, 255]
xcord1 = random.randint(0, xaxis - size)
ycord1 = random.randint(0, yaxis - size)
xcord2 = xcord1 + size
ycord2 = ycord1 + size


while True:
    success, img = capture.read()
    # img = np.zeros((xaxis, yaxis, 3), dtype=np.uint8) #for non-cam
    print('dx=' + str(dx))
    print('dy=' + str(dy))
    print('xcord1 = ' + str(xcord1))
    print('ycord1 = ' + str(ycord1))
    cv2.rectangle(img, (xcord1, ycord1), (xcord2, ycord2), color, thicc)
    xcord1 += dx
    xcord2 += dx
    ycord1 += dy
    ycord2 += dy

    if dx == 1 and dy == 1:
        if xcord1 >= xaxis - thicc - size:
            dx *= -1
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        if ycord1 >= yaxis - thicc - size:
            dy *= -1
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        if xcord1 == xaxis + thicc and ycord1 == yaxis + thicc:
            dx *= -1
            dy *= -1
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    if dx == 1 and dy == -1:
        if xcord1 >= xaxis - thicc - size:
            dx *= -1
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        if ycord1 <= 0 + thicc:
            dy *= -1
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        if xcord1 == xaxis + thicc and ycord1 == 0 + thicc:
            dx *= -1
            dy *= -1
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    if dx == -1 and dy == 1:
        if xcord1 <= 0 + thicc:
            dx *= -1
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        if ycord1 >= yaxis - thicc - size:
            dy *= -1
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        if xcord1 == 0 + thicc and ycord1 == yaxis + thicc:
            dx *= -1
            dy *= -1
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    if dx == -1 and dy == -1:
        if xcord1 <= 0 + thicc:
            dx *= -1
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        if ycord1 <= 0 + thicc:
            dy *= -1
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        if xcord1 == 0 + thicc and ycord1 == 0 + thicc:
            dx *= -1
            dy *= -1
            color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    cv2.imshow('Frame', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()