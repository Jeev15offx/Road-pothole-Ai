from fastapi import FastAPI

app = FastAPI(title="Road Pothole AI API")

@app.get("/")
def root():
    return {"status": "Backend is running"}