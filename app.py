
from flask import Flask, render_template, request, redirect, url_for
import os
from model.dummy_model import predict_image

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ---------------- ROUTES ---------------- #

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return redirect(url_for("prediction"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/prediction", methods=["GET", "POST"])
def prediction():
    result = None
    confidence = None
    image_name = None

    if request.method == "POST":
        if "image" not in request.files:
            return render_template("prediction.html")

        file = request.files["image"]

        if file.filename == "":
            return render_template("prediction.html")

        image_name = file.filename
        path = os.path.join(app.config["UPLOAD_FOLDER"], image_name)
        file.save(path)

        # ✅ Dummy model prediction (FAKE but app runs)
        result, confidence = predict_image(path)

    return render_template(
        "prediction.html",
        result=result,
        confidence=confidence,
        image=image_name
    )


@app.route("/logout")
def logout():
    return render_template("logout.html")


if __name__ == "__main__":
    app.run(debug=True)
