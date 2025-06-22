#!/bin/bash

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# (Optional) Preload DeepFace model
python -c "from deepface import DeepFace; DeepFace.build_model('Emotion')"
