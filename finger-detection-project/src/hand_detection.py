import cv2
class HandDetector:
    def __init__(self, detection_confidence=0.5):
        import mediapipe as mp
        
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=detection_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def detect_hands(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return image, results.multi_hand_landmarks

    def count_fingers(self, hand_landmarks):
        if hand_landmarks:
            # Thumb is counted separately
            thumb_up = hand_landmarks[0].landmark[4].y < hand_landmarks[0].landmark[3].y
            count = 1 if thumb_up else 0
            
            # Count other fingers
            for i in range(1, 5):
                finger_tip = hand_landmarks[0].landmark[4 + i * 4].y
                finger_bottom = hand_landmarks[0].landmark[3 + i * 4].y
                if finger_tip < finger_bottom:
                    count += 1
            return count
        return 0