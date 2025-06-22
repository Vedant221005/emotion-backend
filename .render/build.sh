#!/bin/bash

# Update and install system packages (if needed for DeepFace / OpenCV)
apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# Optional: You can preload DeepFace models here (downloads will cache in Render build)
python -c "
from deepface import DeepFace
DeepFace.build_model('Emotion')
"
