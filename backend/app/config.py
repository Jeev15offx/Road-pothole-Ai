import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")
    ROBOFLOW_MODEL_ID = os.getenv("ROBOFLOW_MODEL_ID")

    EMAIL_SENDER = os.getenv("EMAIL_SENDER")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")

settings = Settings()