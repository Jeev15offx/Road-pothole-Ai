from fastapi import FastAPI
from app.routes.prediction import router as prediction_router

from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="Road Pothole AI API")

app.include_router(prediction_router)
@app.get("/")
def root():
    return {"status": "Backend is running"}