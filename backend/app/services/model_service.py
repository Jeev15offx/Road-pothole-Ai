from inference_sdk import InferenceHTTPClient
import os

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key=os.getenv("ROBOFLOW_API_KEY")
)

def predict_image(image_path: str):
    result = client.infer(
        image_path,
        model_id="Pothole-Detection/2"  # replace with your actual model/version
    )
    return result