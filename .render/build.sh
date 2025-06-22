#!/bin/bash

# Step 1: Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Step 2: Preload the DeepFace emotion model (optional)
python -c "
from deepface import DeepFace
DeepFace.build_model('Emotion')
"
