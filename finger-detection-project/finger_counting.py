import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Define finger tip landmarks (thumb to pinky)
FINGER_TIPS = [4, 8, 12, 16, 20]

# Start video capture
cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame for natural interaction
        frame = cv2.flip(frame, 1)
        h, w, c = frame.shape

        # Convert to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        finger_count = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                lm_list = []
                for id, lm in enumerate(hand_landmarks.landmark):
                    lm_list.append((int(lm.x * w), int(lm.y * h)))

                # Thumb
                if lm_list[FINGER_TIPS[0]][0] > lm_list[FINGER_TIPS[0] - 1][0]:
                    finger_count += 1
                # Other fingers
                for tip in FINGER_TIPS[1:]:
                    if lm_list[tip][1] < lm_list[tip - 2][1]:
                        finger_count += 1

                # Draw hand landmarks
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display finger count
        cv2.rectangle(frame, (0,0), (150,80), (0,0,0), -1)
        cv2.putText(frame, f'Fingers: {finger_count}', (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2)

        cv2.imshow("Finger Counter", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()