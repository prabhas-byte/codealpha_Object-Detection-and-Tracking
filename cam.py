# task4_object_detection_tracking.py
# Real-time object detection + tracking using YOLOv8 (ultralytics)

import cv2
from ultralytics import YOLO
import time

# Load pre-trained YOLOv8 model (nano version - fast and good for real-time)
model = YOLO("yolov8n.pt")

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# Optional: set resolution for better performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

print("Real-time Object Detection & Tracking started.")
print("Press 'q' to quit")

# Variables for FPS calculation
prev_time = time.time()
fps = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame. Exiting...")
        break

    # Run detection + tracking
    results = model.track(
        frame,
        persist=True,               # keep track IDs across frames
        tracker="bytetrack.yaml",   # high-quality built-in tracker
        conf=0.4,                   # minimum confidence
        iou=0.5,                    # IoU threshold
        verbose=False
    )

    # Draw bounding boxes, labels, confidence and tracking IDs
    annotated_frame = results[0].plot()

    # Calculate real FPS
    curr_time = time.time()
    if curr_time - prev_time > 0:
        fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Display FPS
    cv2.putText(
        annotated_frame,
        f"FPS: {int(fps)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv2.LINE_AA
    )

    # Show the result
    cv2.imshow("YOLOv8 Real-Time Detection + Tracking", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
print("Program finished")