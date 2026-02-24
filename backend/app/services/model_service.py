import os
import requests

def predict_image(image_path: str):

    url = "https://api.roboflow.com/workflows/babu-4meph/find-potholes/3"

    params = {
        "api_key": os.getenv("ROBOFLOW_API_KEY")
    }

    with open(image_path, "rb") as f:
        response = requests.post(
            url,
            params=params,
            files={"file": f}
        )

    return response.json()