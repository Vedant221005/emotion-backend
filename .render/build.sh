#!/bin/bash
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 -c "from deepface import DeepFace; DeepFace.build_model('Emotion')"
