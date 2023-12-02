import cv2
from cv2.typing import MatLike
from PIL import Image, ImageDraw
import numpy as np
import json

from ultralytics import YOLO
from config import config

class YoloModel():

    def __init__(self, root_directory: str=config.root_directory, weights: str='yolov8l.pt'):
        self.model = YOLO(weights)
        self.root_directory = root_directory

    def get_boxs(self, image='17.png', thr=0.2):
        
        image_filename = f'./{self.root_directory}/{image}'
        image = np.array(Image.open(image_filename))[:, :, :3].copy()

        results = self.model.predict(source=image, save=False, conf=float(thr))

        for result in results:
            boxes = result.boxes  # Boxes object for bbox outputs
            probs = result.probs  # Probs object for classification outputs
            
            for box in boxes:   
                box = box.xyxy[0]

                point_1 = [int(box[0].item()), int(box[1].item())]
                point_2 = [int(box[2].item()), int(box[3].item())]

                image = cv2.rectangle(image, pt1=point_1, pt2=point_2, color=(255, 0, 255), thickness=3) 

        return image
    


model = YoloModel()
