# 🎥 Task 4: Real-Time Object Detection & Tracking

Your webcam just became a smart eye — detects objects, draws boxes, labels them, and **tracks** them like a pro!

<p align="center">
  <img src="./screenshot-main.png" width="70%" alt="Live YOLOv8 detection + tracking in action">
  <br><b>People walk in → boxes appear → IDs stick → it never forgets who’s who</b>
</p>

## ✨ Features

- **Instant webcam activation** – opens your camera in one run
- Uses **YOLOv8** (nano model) – lightning-fast object detection
- Draws colorful **bounding boxes** + class names (person, car, bottle, phone, laptop…)
- Shows **confidence scores** on every detection
- **Persistent tracking IDs** – same object keeps same ID even if it moves, turns, or gets partially hidden
- Real-time **FPS counter** in top-left corner
- Simple exit: press **q** on keyboard
- Clean & minimal display window – focus on the magic

## Screenshots

![image alt](https://github.com/prabhas-byte/codealpha_Object-Detection-and-Tracking/blob/29e7d22a1df44295b0dc470635dfe4b80ab10007/Screenshot%202026-02-03%20131531.png)
![image alt]()
## 🚀 Quick Start (2 minutes)

### 1. Install Dependencies (one-time)

pip install ultralytics opencv-python

### 2. Run the Script

python filename.py

- Webcam opens automatically
- Detection + tracking starts instantly
- Press q to quit

## 🛠️ Tech Stack

- Python 3.8+
- OpenCV – webcam capture & real-time display
- Ultralytics YOLOv8 – state-of-the-art object detection
- ByteTrack – high-quality built-in tracker (persistent IDs)

No internet needed after first model download (~6 MB)

Pro Tips & Customizations

Edit these lines in task4.py to level it up:
Better accuracy (slightly slower):
model = YOLO("yolov8s.pt")

## ⚙️ Troubleshooting

"Cannot open webcam"
- Close Zoom, Teams, WhatsApp video, or any app using camera
- Restart laptop if still stuck

Model download fails / stuck
- Check internet
- Run again — it auto-downloads yolov8n.pt only once

No boxes appear
- Lower confidence: conf=0.3
- Improve lighting or move closer to camera

Low FPS
- Use yolov8n.pt (fastest model)
- Keep resolution at 640×480 (already set)

Window not showing
- Ensure no other program is blocking OpenCV display

## Credits

- YOLOv8 & ByteTrack – powered by Ultralytics
- OpenCV – real-time video handling

## License

- MIT License – free to use, modify, fork, and build on.
- Made with ❤️ & late-night webcam experiments by Prabhas
- February 2026 🚀
#SeeEverythingTrackEverything
