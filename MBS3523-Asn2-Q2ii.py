import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0);

cv2.namedWindow("Tracking1")
cv2.createTrackbar("LH", "Tracking1", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking1", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking1", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking1", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking1", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking1", 255, 255, nothing)

cv2.namedWindow("Tracking2")
cv2.createTrackbar("LH", "Tracking2", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking2", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking2", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking2", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking2", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking2", 255, 255, nothing)

while True:
    success, frame1 = cap.read()
    frame2 = frame1.copy()

    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Tracking1")
    l_s = cv2.getTrackbarPos("LS", "Tracking1")
    l_v = cv2.getTrackbarPos("LV", "Tracking1")

    u_h = cv2.getTrackbarPos("UH", "Tracking1")
    u_s = cv2.getTrackbarPos("US", "Tracking1")
    u_v = cv2.getTrackbarPos("UV", "Tracking1")

    l_b1 = np.array([l_h, l_s, l_v])
    u_b1 = np.array([u_h, u_s, u_v])

    l_h2 = cv2.getTrackbarPos("LH", "Tracking2")
    l_s2 = cv2.getTrackbarPos("LS", "Tracking2")
    l_v2 = cv2.getTrackbarPos("LV", "Tracking2")

    u_h2 = cv2.getTrackbarPos("UH", "Tracking2")
    u_s2 = cv2.getTrackbarPos("US", "Tracking2")
    u_v2 = cv2.getTrackbarPos("UV", "Tracking2")

    l_b2 = np.array([l_h2, l_s2, l_v2])
    u_b2 = np.array([u_h2, u_s2, u_v2])

    mask1 = cv2.inRange(hsv, l_b1, u_b1)
    mask2 = cv2.inRange(hsv, l_b2, u_b2)

    res1 = cv2.bitwise_and(frame1, frame1, mask=mask1)
    res2 = cv2.bitwise_and(frame2, frame2, mask=mask2)

    mask3 = cv2.add(mask1, mask2)

    contours, hierarchy = cv2.findContours(mask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        (x, y, w, h) = cv2.boundingRect(cnt)
        if area > 100:
            cv2.drawContours(frame1, [cnt], 0, (255, 0, 0), 3)


    cv2.imshow("frame", frame1)
    #cv2.imshow("frame2", frame2)
    cv2.imshow("mask1", mask1)
    cv2.imshow("mask2", mask2)
    #cv2.imshow("mask3", mask3)
    cv2.imshow("res1", res1)
    cv2.imshow("res2", res2)

    key = cv2.waitKey(1)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()