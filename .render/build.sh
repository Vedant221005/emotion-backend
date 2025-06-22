#!/bin/bash

# Upgrade pip and install Python packages
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Preload DeepFace emotion model
python3 -c "from deepface import DeepFace; DeepFace.build_model('Emotion')"
