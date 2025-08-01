from flask import Flask, render_template, request
import cv2
import os
import random
from werkzeug.utils import secure_filename
from chatbot import generate_reply

app = Flask(__name__)

# Configure upload folder
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load Haar cascade for eye detection using full path
CASCADE_PATH = os.path.join(os.path.dirname(__file__), 'haarcascades', 'haarcascade_eye.xml')
if not os.path.exists(CASCADE_PATH):
    raise FileNotFoundError("haarcascade_eye.xml not found in 'haarcascades' directory.")

eye_cascade = cv2.CascadeClassifier(CASCADE_PATH)

def detect_eyes(image_path):
    """Detects eyes in the given image using Haar cascade."""
    img = cv2.imread(image_path)
    if img is None:
        print("Failed to load image.")
        return False

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    print(f"Detected {len(eyes)} eyes.")
    return len(eyes) > 0

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    chatbot_reply = None
    user_message = ""

    if request.method == "POST":
        if "image" in request.files and request.files["image"].filename != "":
            image = request.files["image"]
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)

            love_detected = detect_eyes(image_path)
            result = "love" if love_detected else "no-love"

        elif "user_message" in request.form:
            user_message = request.form["user_message"].strip()
            if user_message:
                chatbot_reply = generate_reply(user_message)

    return render_template("index.html", result=result, chatbot_reply=chatbot_reply, user_message=user_message)

if __name__ == "__main__":
    app.run(debug=True)
