
from fastapi import APIRouter, UploadFile, File
from app.services.inference_service import run_inference
from app.schemas.prediction_schema import PredictionResponse, BoundingBox

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    contents = await file.read()

    detections = await run_inference(contents)

    return {
        "filename": file.filename,
        "detections": detections
    }