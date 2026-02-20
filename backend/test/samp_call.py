from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="S9zy6oG5Kp1FtzScLNKk"
)

result = client.run_workflow(
    workspace_name="babu-4meph",
    workflow_id="find-potholes",
    images={"image": "path/to/image.jpg"},
    use_cache=True
)

print(result)