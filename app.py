
# from flask import Flask, render_template, request, redirect
# import numpy as np
# # from tensorflow.keras.models import load_model   # ❌ model loading बंद
# from tensorflow.keras.preprocessing.image import load_img, img_to_array

# app = Flask(__name__)

# # ❌ Invalid model file मुळे ही line comment केली
# # model = load_model("model/Updated-Xception-diabetic-retinopathy.h5")

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/login', methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         return redirect('/prediction')
#     return render_template("login.html")

# @app.route('/register', methods=['GET','POST'])
# def register():
#     if request.method == 'POST':
#         return redirect('/login')
#     return render_template("register.html")

# @app.route('/prediction', methods=['GET','POST'])
# def prediction():
#     result = None
#     if request.method == 'POST':
#         file = request.files['image']
#         path = "static/uploads/" + file.filename
#         file.save(path)

#         img = load_img(path, target_size=(224,224))
#         img = img_to_array(img)
#         img = np.expand_dims(img, axis=0)
#         img = img / 255.0

#         # ❌ model.predict() काढलं
#         # pred = model.predict(img)
#         # result = np.argmax(pred)

#         # ✅ Temporary demo result
#         result = "Diabetic Retinopathy Detected"

#     return render_template("prediction.html", result=result)

# @app.route('/logout')
# def logout():
#     return render_template("logout.html")

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask, render_template, request, redirect
# import numpy as np
# import os
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.image import load_img, img_to_array

# app = Flask(__name__)

# # Upload folder
# UPLOAD_FOLDER = 'static/uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Load your trained Xception model
# # model_path = "model/Updated-Xception-diabetic-retinopathy.h5"
# # model = load_model(model_path)
# model = load_model("model")


# # Class mapping
# classes = {
#     0: "Normal",
#     1: "Mild DR",
#     2: "Moderate DR",
#     3: "Severe DR",
#     4: "Proliferative DR"
# }

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/login', methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         return redirect('/prediction')
#     return render_template("login.html")

# @app.route('/register', methods=['GET','POST'])
# def register():
#     if request.method == 'POST':
#         return redirect('/login')
#     return render_template("register.html")

# @app.route('/prediction', methods=['GET','POST'])
# def prediction():
#     result = None
#     confidence = None
#     image_filename = None

#     if request.method == 'POST':
#         file = request.files['image']
#         if file and file.filename != '':
#             image_filename = file.filename
#             path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
#             file.save(path)

#             # Load and preprocess image (Xception expects 229x229)
#             img = load_img(path, target_size=(229,229))
#             img_array = img_to_array(img)
#             img_array = np.expand_dims(img_array, axis=0)
#             img_array = img_array / 255.0

#             # Predict
#             pred = model.predict(img_array)
#             class_index = np.argmax(pred)
#             confidence = np.max(pred)

#             result = classes[class_index]

#     return render_template("prediction.html",
#                            result=result,
#                            confidence=confidence,
#                            image=image_filename)

# @app.route('/logout')
# def logout():
#     return render_template("logout.html")

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for
# import numpy as np
# import os
# from tensorflow.keras.models import load_model
# from model.dummy_model import predict_image

# from tensorflow.keras.preprocessing.image import load_img, img_to_array

# app = Flask(__name__)

# # Upload folder
# UPLOAD_FOLDER = os.path.join("static", "uploads")
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# # 🔴 LOAD MODEL (REAL .h5 FILE REQUIRED)
# model = load_model("Updated-Xception-diabetic-retinopathy.h5")

# # Class labels
# classes = {
#     0: "Normal",
#     1: "Mild DR",
#     2: "Moderate DR",
#     3: "Severe DR",
#     4: "Proliferative DR"
# }

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         return redirect(url_for("prediction"))
#     return render_template("login.html")

# @app.route("/register", methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         return redirect(url_for("login"))
#     return render_template("register.html")

# @app.route("/prediction", methods=["GET", "POST"])
# def prediction():
#     result = None
#     confidence = None
#     image_name = None

#     if request.method == "POST":
#         if "image" not in request.files:
#             return render_template("prediction.html")

#         file = request.files["image"]
#         if file.filename == "":
#             return render_template("prediction.html")

#         image_name = file.filename
#         path = os.path.join(app.config["UPLOAD_FOLDER"], image_name)
#         file.save(path)

#         # Image preprocessing (Xception)
#         img = load_img(path, target_size=(229, 229))
#         img_array = img_to_array(img)
#         img_array = np.expand_dims(img_array, axis=0)
#         img_array = img_array / 255.0

#         # Prediction
#         pred = model.predict(img_array)
#         class_index = int(np.argmax(pred))
#         confidence = round(float(np.max(pred)) * 100, 2)
#         result = classes[class_index]

#     return render_template(
#         "prediction.html",
#         result=result,
#         confidence=confidence,
#         image=image_name
#     )

# @app.route("/logout")
# def logout():
#     return render_template("logout.html")

# if __name__ == "__main__":
#     app.run(debug=True)







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
