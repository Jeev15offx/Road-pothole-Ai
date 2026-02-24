from inference_sdk import InferenceHTTPClient
import base64
import os

image_path = "NH.jpg"
print("Exists:", os.path.exists(image_path))
print("Absolute path:", os.path.abspath(image_path))
client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="S9zy6oG5Kp1FtzScLNKk"
)

result = client.run_workflow(
    workspace_name="babu-4meph",
    workflow_id="find-potholes",
    images={"image": "road.jpg"}   # <-- STRING PATH
)
print(result)

''' predictions = result[0]["predictions"]["predictions"]
img = result[0]["predictions"]["image"]

IMAGE_AREA = img["width"] * img["height"]

SIGNIFICANT_RATIO = 0.01  # 1% of image
CONF_THRESHOLD = 0.6

valid = []

for p in predictions:
    pothole_area = p["width"] * p["height"]
    ratio = pothole_area / IMAGE_AREA

   # print("Ratio:", ratio, "Confidence:", p["confidence"])

    if ratio > SIGNIFICANT_RATIO and p["confidence"] > CONF_THRESHOLD:
        valid.append(p)

if valid:
    print("🕳️ Significant pothole detected")
else:
    print("✅ No significant pothole") '''