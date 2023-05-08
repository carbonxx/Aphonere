import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import math

cap = cv2.VideoCapture(0)

detector = HandDetector(maxHands=1)
classifier = Classifier("Test\keras_model.h5", "Test\labels.txt")

offset = 20
imgSize = 300

labels = ["Hello", "I'm", "C", "A", "R", "O", "L"]

while True:
    success, img = cap.read()

    imgOutput = img.copy()

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        (x, y), (w, h) = hand['bbox'][:2], hand['bbox'][2:]

        imgWhite = np.zeros((imgSize, imgSize, 3), np.uint8)
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgResize = cv2.resize(imgCrop, (imgSize, imgSize), interpolation=cv2.INTER_AREA)
        prediction, index = classifier.getPrediction(imgResize, draw=False)

        cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)

    cv2.imshow("Image", imgOutput)

    key = cv2.waitKey(1)

    if key == ord("Q"):
        break

    elif key == 27:
        # ESC 
        print("\n")

    elif key == 32:
        # SPACE 
        print(labels[index] + " ", end='')

    elif key == 13:
        # ENTER 
        print(labels[index], end='')

cv2.destroyAllWindows()
cap.release()

        