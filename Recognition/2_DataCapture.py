import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

counter = 0
folder = "D:\ISL-main\Recognition\Data"
image_size = (300, 300)

cap = cv2.VideoCapture(0)
success, img = cap.read()
if not success:
    raise Exception("Failed to read from camera")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, image_size)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    start_time = time.time()
    while cap.isOpened():
        success, img = cap.read()

        if not success:
            print("Ignoring empty camera frame.")
            continue

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, image_size)
        img = img.astype('uint8')

        results = hands.process(img)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    img,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())

            if time.time() - start_time >= 0.01:
                counter += 1
                cv2.imwrite(f'{folder}/Image_{counter}.jpg', img)
                print(counter)
                start_time = time.time()

        cv2.imshow("Image", cv2.flip(img, 1))
        key = cv2.waitKey(1)
        if key == ord("Q"):
            break