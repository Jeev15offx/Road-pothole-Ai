# 1. Import the library
from inference_sdk import InferenceHTTPClient

# 2. Connect to your workflow
client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="S9zy6oG5Kp1FtzScLNKk"
)

# 3. Run your workflow on an image
result = client.run_workflow(
    workspace_name="babu-4meph",
    workflow_id="find-potholes",
    images={
        "image": "road.jpg" # Path to your image file
    },
    use_cache=True # Speeds up repeated requests
)

# 4. Get your results
#print(result)

preds = result[0]["predictions"]["predictions"]

MIN_AREA = 5000  # adjust based on testing

significant = []

for p in preds:
    area = p["width"] * p["height"]
    if area >= MIN_AREA:
        significant.append(p)

if len(significant) == 0:
    print("No significant pothole")
else:
    print("Significant pothole detected")
''' if len(preds) == 0:
    print("No pothole detected")
else:
    print("Pothole detected")
 '''
