!pip install ultralytics==8.0.196 roboflow

# YOLO 라이브러리 임포트
from roboflow import Roboflow

# API 키를 사용하여 Roboflow 객체 생성
rf = Roboflow(api_key="qDWPbQf6Pql7N7ewfUbF")


project = rf.workspace("heeju-qtcpj").project("ml-q1vth")
version = project.version(1)

# YOLOv8 형식으로 데이터셋 다운로드
dataset = version.download("yolov8")

from ultralytics import YOLO

# YOLOv8 모델 불러오기
model = YOLO('yolov8n.yaml') 

# 데이터 경로 설정
data_path = dataset.location + '/data.yaml' 

# 모델 훈련
model.train(data=data_path, epochs=100, imgsz=640)