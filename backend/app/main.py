from fastapi import FastAPI
from app.routes.prediction import router as prediction_router

from dotenv import load_dotenv
load_dotenv()

from dotenv import load_dotenv
import os

load_dotenv()
print("API KEY:", os.getenv("ROBOFLOW_API_KEY"))

app = FastAPI(title="Road Pothole AI API")

app.include_router(prediction_router)
@app.get("/")
def root():
    return {"status": "Backend is running"}