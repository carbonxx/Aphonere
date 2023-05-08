# import cv2
# from cvzone.HandTrackingModule import HandDetector
# from cvzone.ClassificationModule import Classifier
# import numpy as np
# import math
# # import time

# cap = cv2.VideoCapture(0)
# detector = HandDetector(maxHands=1)
# classifier = Classifier("F:\Aphonere\Aphonere\Recognition\Data\Model\keras_model.h5", "F:\Aphonere\Aphonere\Recognition\Data\Model\labels.txt")

# offset = 20
# imgSize = 300

# counter = 0

# labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# while True:
#     success, img = cap.read()
#     imgOutput = img.copy()
#     hands, img = detector.findHands(img)
#     if hands:
#         hand = hands[0]
#         x, y, w, h = hand['bbox']
#         imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
#         imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
#         imgCropShape = imgCrop.shape
#         aspectRatio = h / w
#         if aspectRatio > 1:
#             k = imgSize / h
#             wCal = math.ceil(k * w)
#             imgResize = cv2.resize(imgCrop, (wCal, imgSize))
#             imgResizeShape = imgResize.shape
#             wGap = math.ceil((imgSize - wCal) / 2)
#             imgWhite[:, wGap:wCal + wGap] = imgResize
#             prediction, index = classifier.getPrediction(imgWhite, draw=False)
#             # print(prediction, index)
#         else:
#             k = imgSize / w
#             hCal = math.ceil(k * h)
#             imgResize = cv2.resize(imgCrop, (imgSize, hCal))
#             imgResizeShape = imgResize.shape
#             hGap = math.ceil((imgSize - hCal) / 2)
#             imgWhite[hGap:hCal + hGap, :] = imgResize
#             prediction, index = classifier.getPrediction(imgWhite, draw=False)
#         # cv2.rectangle(imgOutput, (x - offset, y - offset - 50),(x - offset + 90, y - offset - 50 + 50), (255, 0, 255), cv2.FILLED)
#         cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)
#         # cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (0, 0, 0), 4)

#         img_counter = 0
#         k = cv2.waitKey(1)
#         if k % 256 == 27:
#             # ESC pressed
#             print("\n")
#             img_counter += 1
#         if k % 256 == 32:
#             # SPACE pressed - Space is added
#             print(labels[index] + " ", end='')
#             img_counter += 1
#         if k % 256 == 8:
#             # BACKSPACE pressed - Letter is removed
#             print("---")
#         elif k % 256 == 13:
#             # ENTER pressed - Concatenation
#             print(labels[index], end='')
#             img_counter += 1

#         # print(labels[index])
#         # cv2.imshow("ImageCrop", imgCrop)
#         # cv2.imshow("ImageWhite", imgWhite)

#     cv2.imshow("Image", imgOutput)
#     key = cv2.waitKey(1)
#     if key == ord("Q"):
#         break


import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
classifier = Classifier("F:\Aphonere\Aphonere\Recognition\Data\Model\keras_model.h5", "F:\Aphonere\Aphonere\Recognition\Data\Model\labels.txt")

offset = 20
imgSize = 300

counter = 0

labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)
    if hands:
        bbox = [hand['bbox'] for hand in hands]
        x_min, y_min = np.min(bbox, axis=0)[:2]
        x_max, y_max = np.max(bbox, axis=0)[2:4]
        w = x_max - x_min
        h = y_max - y_min
        center_x = int((x_min + x_max) / 2)
        center_y = int((y_min + y_max) / 2)
        size = int((w + h) / 2)

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y_min - offset:y_max + offset, x_min - offset:x_max + offset]
        imgCropShape = imgCrop.shape
        aspectRatio = h / w
        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)

        cv2.putText(imgOutput, labels[index], (center_x, center_y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 0, 0), 2)

    cv2.imshow("Image", imgOutput)
    key = cv2.waitKey(1)
    if key == ord("Q"):
        break
