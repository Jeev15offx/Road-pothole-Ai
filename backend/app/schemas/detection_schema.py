from pydantic import BaseModel
                
class DetectionRequest(BaseModel):
    image_base64: str
    latitude: float
    longitude: float