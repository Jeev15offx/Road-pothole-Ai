from flask import Flask, request, jsonify
from inference_sdk import InferenceHTTPClient
import os

app = Flask(__name__)

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=os.getenv("S9zy6oG5Kp1FtzScLNKk")
)

@app.route("/detect", methods=["POST"])
def detect():
    file = request.files["image"]
    temp_path = f"temp_{file.filename}"
    file.save(temp_path)

    result = client.run_workflow(
        workspace_name="babu-4meph",
        workflow_id="find-potholes",
        images={"image": temp_path}
    )

    os.remove(temp_path)
    return jsonify(result)

app.run(port=5000, debug=True)