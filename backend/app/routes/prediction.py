from fastapi import APIRouter, UploadFile, File
import shutil
import os
from app.services.model_service import predict_image

router = APIRouter()

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    
    upload_dir = "temp"
    os.makedirs(upload_dir, exist_ok=True)
    
    file_path = os.path.join(upload_dir, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    prediction = predict_image(file_path)

    # Clean up the temporary file

    os.remove(file_path)
    return {"predictions": prediction}
