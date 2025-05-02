import cv2
from hand_detection import HandDetector

def main():
    # Initialize the camera feed
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        # Detect hands and count fingers
        hands = detector.detect_hands(frame)
        finger_count = detector.count_fingers(hands)

        # Display the number of fingers detected
        cv2.putText(frame, f'Fingers: {finger_count}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Show the frame with the detection
        cv2.imshow('Finger Detection', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()