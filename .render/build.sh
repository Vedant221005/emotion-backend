#!/bin/bash

# Step 1: Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Step 2: Install system-level dependencies (for OpenCV / DeepFace)
apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# Step 3: Preload the DeepFace emotion model (optional)
python -c "
from deepface import DeepFace
DeepFace.build_model('Emotion')
"
