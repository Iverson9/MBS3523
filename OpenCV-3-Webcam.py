import cv2

capture = cv2.VideoCapture(0)
capture.set(3, 640)
capture.set(4, 480)

while True:
    success, img = capture.read()
    cv2.imshow('Frame', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break
capture.release()
cv2.destroyAllWindows()