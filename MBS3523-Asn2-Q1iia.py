from imutils import paths
import  face_recognition
import cv2
import os
import pickle

imagePaths = list(paths.list_images('known_image'))
knownEncodings = []
knownNames = []
for(i, imagePaths) in enumerate(imagePaths):
    name = imagePaths.split(os.path.sep)[1]
    suffix = os.path.splitext(imagePaths)[1]
    name = name.replace(suffix, '')
    print(name)
    image = cv2.imread(imagePaths)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)
    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)
data = {"encodings": knownEncodings, "names": knownNames}
f = open("face_enc", "wb")
f.write(pickle.dumps(data))
f.close()