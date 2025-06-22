#!/bin/bash

# Upgrade pip and install Python packages
pip install --upgrade pip
pip install -r requirements.txt

# Preload DeepFace emotion model
python -c "from deepface import DeepFace; DeepFace.build_model('Emotion')"
