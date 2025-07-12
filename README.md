# SkinVisionAI 🧠🌿  
A Deep Learning–Powered Web App for Skin Cancer Detection

## 🚀 Overview
SkinVisionAI is a smart diagnostic tool built using Convolutional Neural Networks (CNNs) to **detect skin cancer** from medical images. This project integrates **deep learning**, **Flask web development**, and  to provide real-time predictions based on user-uploaded skin lesion images.

The goal is to assist dermatological screening through intelligent automation, promoting early detection and awareness.

---

## 🔍 Features

- 🧠 Trained CNN model for classifying skin lesions (cancerous vs non-cancerous)  
- 🌐 Flask-based web interface for live user input and results  
- 📷 Image preprocessing pipeline with resizing, normalization, and prediction   
- 📊 Accuracy-optimized with model tuning and data augmentation

---

## 🧑‍💻 Tech Stack

| Layer              | Tools Used                           |
|--------------------|--------------------------------------|
| Language           | Python                               |
| Machine Learning   | TensorFlow, Keras, NumPy, OpenCV     |
| Web Framework      | Flask                                |
| Frontend           | HTML, CSS                            |
| Model File         | `model.h5` (trained CNN model)       |
| Deployment Ready   | AWS S3 / EC2 compatible              |

---

## 📁 File Structure

├── app.py # Flask app backend
├── cancerdet.ipynb # CNN model training and evaluation
├── flask import python code.py # Alternate Flask logic (if relevant)
├── model.h5 # Trained CNN model
├── README.md # Project documentation
└── static/ # (Optional) Frontend assets
