#!/bin/bash

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Preload DeepFace model (optional)
python3 -c "from deepface import DeepFace; DeepFace.build_model('Emotion')"
