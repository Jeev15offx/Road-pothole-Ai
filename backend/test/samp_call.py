from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="S9zy6oG5Kp1FtzScLNKk"
)

result = client.run_workflow(
    workspace_name="babu-4meph",
    workflow_id="find-potholes",
    images={"image": "Road-pothole-Ai/backend/test/img-79.jpg"},
    use_cache=True
)

print(result)