# UAV Object Detection with YOLOv8

This repository contains the first version of an object detection system developed for a UAV (Unmanned Aerial Vehicle) project during an internship. The system is built using **YOLOv8** and a custom-trained model trained on a dataset from **Roboflow Universe**. It detects a variety of objects, including cars, cell phones, water bodies, fire, birds, planes, rockets, buses, persons, laptops, and more. Designed for real-time detection, it has been tested with a webcam and is intended for UAV applications such as environmental monitoring, surveillance, or navigation.

## Features
- Real-time object detection using YOLOv8.
- Custom-trained model (`best.pt`) for diverse object classes.
- Webcam input for testing, adaptable for UAV camera feeds.
- Lightweight and extensible for drone deployment.

## Directory Structure
```
uav-object-detection/
├── Yolov8m/
│   └── weights/
│       └── best.pt     # Custom-trained YOLOv8 model
├── detect.py           # Main script for real-time detection
├── args.yaml           # Configuration file for YOLOv8 training/inference
├── Yolov8m.pt          # Pretrained YOLOv8 medium model
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

## Prerequisites
- Python 3.8+
- OpenCV (`cv2`)
- Ultralytics YOLOv8
- A webcam or video file for testing
- (Optional) NVIDIA GPU with CUDA for faster inference

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/BinaryFighter-01/uav-object-detection.git
   cd uav-object-detection
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is missing, install core libraries:
   ```bash
   pip install ultralytics opencv-python
   ```

4. **Verify model file**:
   Ensure `Yolov8m/weights/best.pt` is present in the repository. This is the custom-trained model.

## Usage
1. **Run the detection script**:
   ```bash
   python detect.py
   ```
   This will:
   - Load the `Yolov8m/weights/best.pt` model.
   - Start real-time detection using your webcam (default input).
   - Display the video feed with detected objects annotated.

2. **Customize input**:
   To use a video file instead of a webcam, modify the `cv2.VideoCapture` line in `detect.py`:
   ```python
   cap = cv2.VideoCapture('path/to/your/video.mp4')
   ```

3. **Exit**:
   Press `q` while the video window is active to stop detection.

## File Descriptions
- **`detect.py`**: Main script for running real-time object detection.
- **`Yolov8m/weights/best.pt`**: Custom-trained YOLOv8 model for your dataset.
- **`Yolov8m.pt`**: Pretrained YOLOv8 medium model (used as a starting point for training).
- **`args.yaml`**: Configuration file for training or inference settings (e.g., model parameters, dataset paths).
- **`requirements.txt`**: Lists Python dependencies required for the project.

## Model Details
- **Base Model**: YOLOv8 (medium variant, fine-tuned).
- **Training Data**: Custom dataset from Roboflow Universe.
- **Classes**: Cars, cell phones, water bodies, fire, birds, planes, rockets, buses, persons, laptops, and more.
- **Weights**: `best.pt` (located in `Yolov8m/weights/`).

## Notes for UAV Deployment
- The current script is designed for testing on a local machine. For UAV integration:
  - Replace webcam input with a drone camera feed (e.g., RTSP stream: `rtsp://<drone-ip>/stream`).
  - Optimize for lightweight models (e.g., YOLOv8n) if deploying on edge devices like Jetson Nano.
  - Account for UAV hardware constraints (power, compute).
- Use `args.yaml` to adjust inference settings (e.g., confidence threshold) for better performance.

## Future Improvements
- Add support for UAV-specific video streams (e.g., RTSP, MAVLink).
- Implement object tracking for consistent detection across frames.
- Optimize model for edge devices (e.g., quantization, pruning).
- Include model evaluation metrics (e.g., mAP, precision, recall).

## Contributing
This is an internship project, but contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Submit a pull request with a clear description.

## License
[MIT License](LICENSE).

## Acknowledgments
- **Ultralytics** for the YOLOv8 framework.
- **Roboflow Universe** for the annotated dataset.
- Internship team for support and guidance.

---
