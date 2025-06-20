# api/detect_emotion.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
from deepface import DeepFace

app = Flask(__name__)
CORS(app)

@app.route("/api/detect_emotion", methods=["POST"])
def detect_emotion():
    try:
        data = request.json
        image_data = data["image"]

        encoded_data = image_data.split(',')[1]
        nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) == 0:
            return jsonify({"emotion": "no_face"})

        result = DeepFace.analyze(img_path=img, actions=["emotion"], enforce_detection=False)
        dominant_emotion = result[0]["dominant_emotion"]

        return jsonify({"emotion": dominant_emotion})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# for local testing only
if __name__ == "__main__":
    app.run(debug=True)
