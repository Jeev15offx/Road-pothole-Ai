from inference_sdk import InferenceHTTPClient
import base64
import os

image_path = "road.jpg"
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

# Extract visualization image
''' base64_image = result["outputs"][0]["visualization"]["value"]

# Decode and save
with open("annotated.jpg", "wb") as f:
    f.write(base64.b64decode(base64_image))

print("Annotated image saved as annotated.jpg") '''
print(result)