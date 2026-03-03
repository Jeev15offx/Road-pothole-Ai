from fastapi import APIRouter
from app.schemas.detection_schema import DetectionRequest
from app.services.inference_service import run_inference
from app.services.notification_service import send_notification

router = APIRouter()

@router.post("/detect")
async def detect_pothole(data: DetectionRequest):

    predictions = run_inference(data.image_base64)

    pothole_detected = False
    confidence = 0

    for pred in predictions:
        if pred["class"] == "pothole" and pred["confidence"] > 0.5:
            pothole_detected = True
            confidence = pred["confidence"]

    if pothole_detected:
        send_notification(
            latitude=data.latitude,
            longitude=data.longitude,
            confidence=confidence
        )

    return {
        "detected": pothole_detected,
        "confidence": confidence
    }