from ultralytics import YOLO
import cv2


# Data Annoted from roboflow Universe


# Load the YOLOv8 model
model = YOLO('yolov8m.pt')  # Ensure the .pt file is in the same directory

# Open video stream or load an image
cap = cv2.VideoCapture(0)  # Change 0 to the path of a video file for testing

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference
    results = model(frame)

    # Visualize the detections on the frame
    annotated_frame = results[0].plot()

    cv2.imshow('YOLOv8 Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
