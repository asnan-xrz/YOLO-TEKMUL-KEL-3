from ultralytics import YOLO

model = YOLO("yolo11m_custom.pt")

model.predict(source = "2-wildlife.mp4", show=True, save=True, classes=[0,1])