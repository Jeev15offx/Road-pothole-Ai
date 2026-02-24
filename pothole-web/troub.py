''' from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="S9zy6oG5Kp1FtzScLNKk"
)

def detectpothole(image_path):

    try:
        result = client.run_workflow(
            workspace_name="babu-4meph",
            workflow_id="find-potholes",
            images={"image": image_path},
            use_cache=True
        )

        # ---- correct extraction ----
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

    except Exception as e:
        return f"Error: {str(e)}" '''
from inference_sdk import InferenceHTTPClient

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key="S9zy6oG5Kp1FtzScLNKk"
)

def detectpothole(image_path):

    try:
        result = client.run_workflow(
            workspace_name="babu-4meph",
            workflow_id="find-potholes",
            images={"image": image_path},
            use_cache=True
        )

        #print("RAW RESULT:", result)  # 👈 debug

        # Get predictions safely
        preds = result[0]["predictions"]["predictions"]

        if not preds:
            return "No pothole detected"

        MIN_AREA = 5000
        significant = []

        for p in preds:
            width = p.get("width")
            height = p.get("height")

            if width is None or height is None:
                continue

            area = width * height

            if area >= MIN_AREA:
                significant.append(p)

        if len(significant) == 0:
            return "No significant pothole"
        else:
            return "Significant pothole detected"

    except Exception as e:
        print("ERROR:", e)
        return "Detection failed"