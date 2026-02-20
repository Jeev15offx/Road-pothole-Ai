from pydantic import BaseModel
from typing import List

class BoundingBox(BaseModel):
    x: float
    y: float
    width: float
    height: float
    confidence: float
    class_name: str

class PredictionResponse(BaseModel):
    filename: str
    detections: List[BoundingBox]