from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="YOUR_NEW_API_KEY"  # paste your NEW key here
)

def predict_image(image_path):
    result = client.infer(
        image_path,
        model_id="pothole-detection-irs11/2"
    )
    return result