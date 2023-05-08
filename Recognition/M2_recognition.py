import cv2
import numpy as np
import math
import time
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("D:\ISL-main\Aphonere\Model\M2_model\keras_model.h5",
                        "D:\ISL-main\Aphonere\Model\M2_model\labels.txt")

offset = 20
imgSize = 300
labels = ["Good", "Day", "Morning", "Afternoon", "Evening", "Night"]

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgResize = cv2.resize(imgCrop, (imgSize, imgSize), interpolation=cv2.INTER_AREA)
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgWhite[(imgSize - imgResize.shape[0]) // 2:(imgSize - imgResize.shape[0]) // 2 + imgResize.shape[0],
        (imgSize - imgResize.shape[1]) // 2:(imgSize - imgResize.shape[1]) // 2 + imgResize.shape[1]] = imgResize

        prediction, index = classifier.getPrediction(imgWhite, draw=False)

        # Use numpy slicing instead of cv2.putText
        cv2.rectangle(imgOutput, (x - 10, y - 40), (x + 110, y - 10), (255, 255, 255), cv2.FILLED)
        cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)

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

    cv2.imshow("Image", imgOutput)
