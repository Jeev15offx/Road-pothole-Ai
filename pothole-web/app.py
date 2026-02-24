from flask import Flask, render_template, request
import os
from troub import detectpothole

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# create uploads folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    result_text = None

    if request.method == "POST":

        file = request.files["image"]

        if file and file.filename != "":
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)

            # just call function — it already returns final message
            result_text = detectpothole(path)
            print("RESULT SENT TO HTML:", result_text)

    return render_template("index.html", result=result_text)


if __name__ == "__main__":
    app.run(debug=True)