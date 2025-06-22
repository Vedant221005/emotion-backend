from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
from deepface import DeepFace

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return "Emotion Detection Backend is Running!"

@app.route("/detect_emotion", methods=["POST"])
def detect_emotion():
    try:
        data = request.json
        image_data = data["image"]

        # Decode the base64 image
        encoded_data = image_data.split(',')[1]
        nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Analyze emotion using DeepFace
        result = DeepFace.analyze(img_path=img, actions=["emotion"], enforce_detection=True)
        dominant_emotion = result[0]["dominant_emotion"]
        return jsonify({"emotion": dominant_emotion})

    except Exception as e:
        if "Face could not be detected" in str(e):
            return jsonify({"emotion": "no_face"})
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
