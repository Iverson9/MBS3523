from imutils import paths
import  face_recognition
import cv2
import os
import pickle

faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
data = pickle.loads(open('face_enc', "rb").read())

webcam = cv2.VideoCapture(0)

while True:
    sucess, img = webcam.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=5, minSize=(60,60), flags=cv2.CASCADE_SCALE_IMAGE)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(imgRGB)
    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"
        if True in matches:
            matchedIDxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}
            for i in matchedIDxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1
            name = max(counts, key=counts.get)
        names.append(name)
        for((x, y, w, h), name) in zip(faces, names):
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()