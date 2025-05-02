def resize_image(image, width, height):
    return cv2.resize(image, (width, height))

def draw_landmarks(image, landmarks, color=(0, 255, 0), thickness=2):
    for landmark in landmarks:
        x, y = int(landmark[0]), int(landmark[1])
        cv2.circle(image, (x, y), 5, color, thickness)