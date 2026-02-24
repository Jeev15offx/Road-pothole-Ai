from flask import Flask, render_template, request
import os
import troub

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# YOUR DETECTION FUNCTION
def detect_pothole(image_path):

    # ---- call your roboflow code here ----
    result = your_detection_function(image_path)

    preds = result[0]["predictions"]["predictions"]

    MIN_AREA = 5000

    significant = [
        p for p in preds if p["width"] * p["height"] >= MIN_AREA
    ]

    if len(significant) == 0:
        return "No Significant Pothole"
    else:
        return "Significant Pothole Detected"


@app.route("/", methods=["GET", "POST"])
def index():

    result_text = None

    if request.method == "POST":
        file = request.files["image"]
        path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(path)

        result_text = detect_pothole(path)

    return render_template("index.html", result=result_text)


if __name__ == "__main__":
    app.run(debug=True)