import cv2, random

carCascade = cv2.CascadeClassifier('Resources\haarcascade_car.xml')
fullbodyCascade = cv2.CascadeClassifier('Resources\haarcascade_fullbody.xml')
capture = cv2.VideoCapture('Resources/MBS3523-Asn1-Q3video2.mp4')

while True:
    success, img = capture.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    body = fullbodyCascade.detectMultiScale(imgGray, 1.1, 3)
    car = carCascade.detectMultiScale(imgGray, 1.2, 4)
    for (x, y, w, h) in body:
        cv2.rectangle(img, (x, y), (x + w, y + h), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)
        cv2.putText(img, 'BODY', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    for (x2, y2, w2, h2) in car:
        cv2.rectangle(img, (x2, y2), (x2 + w2, y2 + h2), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), 2)
        cv2.putText(img, 'CAR', (x2, y2 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break
