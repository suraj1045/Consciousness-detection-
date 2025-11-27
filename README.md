# Consciousness-detection-
<<<<<<< HEAD
A real-time driver alertness monitoring system using the YOLOv5 deep learning framework for detecting states of consciousness ("awake" vs. "drowsy"). Implemented live video feed analysis with high detection accuracy and minimal latency, leveraging computer vision techniques. The system was designed to figure out the state of awareness of a person.

## the command to run this project 
python yolo/yolov5/detect.py \
    --weights <path to the folder>/Consciousness-detection-/yolo/yolov5/runs/train/fast_drowsy_detector_m33/weights/best.pt \
    --source 0 \
    --img 256 \
    --conf 0.5 \
    --device mps
>>>>>>> 98f1040 ( resrtuctured the data set)
