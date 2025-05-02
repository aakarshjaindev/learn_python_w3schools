# Finger Detection Project

This project implements a real-time finger detection system using a live camera feed. It utilizes computer vision techniques to detect hands and count the number of fingers shown.

## Project Structure

```
finger-detection-project
├── src
│   ├── main.py            # Entry point of the application
│   ├── hand_detection.py   # Contains HandDetector class for hand detection
│   ├── utils
│   │   └── helpers.py     # Utility functions for image processing
├── requirements.txt       # Lists project dependencies
└── README.md              # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd finger-detection-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will initialize the camera feed and display the number of fingers detected in real-time.

## Functionality

- **Hand Detection**: The application processes the camera feed to identify hands using the `HandDetector` class.
- **Finger Counting**: It counts the number of fingers shown using the `count_fingers` method.
- **Real-time Display**: The results are displayed in real-time on the camera feed.

## Dependencies

The project requires the following libraries:
- OpenCV
- Any additional libraries specified in `requirements.txt`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.