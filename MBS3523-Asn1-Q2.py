import cv2, random, numpy as np


capture = cv2.VideoCapture(0)

width = 640
height = 480
size = 80 # size of the square (must be within x y)
thicc = 3 # thickness of the square
color = [255, 255, 255]
xc1 = random.randint(0, width - size)
yc1 = random.randint(0, height - size)
xc2 = xc1 + size
yc2 = yc1 + size
dx = 1
dy = 1

while True:
    success, img = capture.read(0)
    #img = np.zeros((height, width, 3), dtype=np.uint8) #for non-cam
    cv2.rectangle(img, (xc1, yc1), (xc2, yc2), color, thicc)
    xc1 += dx
    xc2 += dx
    yc1 += dy
    yc2 += dy
    if xc1 >= width - size - thicc or xc1 <= 0:
        dx = dx * (-1)
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    if yc1 >= height - size - thicc or yc1 <= 0:
        dy = dy * (-1)
        color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

    cv2.imshow('Frame', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
