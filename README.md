# Housing Price Prediction

This project demonstrates an end-to-end pipeline for building, deploying, and serving a machine learning-powered real estate price prediction website. It combines data science workflows, a Flask backend, an HTML/JavaScript frontend, and deployment using AWS EC2 and NGINX.

---

## 🚀 Project Overview

**Goal:** Predict home prices using regression and serve predictions through a web interface.

**Components:**
- Data preprocessing and model building (Python, pandas, NumPy, scikit-learn)
- REST API backend (Flask)
- Web frontend (HTML, CSS, JavaScript)
- Production deployment (AWS EC2, Ubuntu, NGINX)

GitHub Repository: [Housing-Price-Prediction](https://github.com/taranroyyuru/Housing-Price-Prediction)

---

## 🧠 Data Science & Model Training

**Dataset:** Custom or public dataset (e.g., [Bangalore Home Prices](https://www.kaggle.com/datasets))

**Steps:**
1. Data ingestion & cleaning
2. Outlier detection & removal
3. Feature engineering & dimensionality reduction
4. Train/test split, GridSearchCV, K-Fold Cross Validation
5. Model persistence (`model.pkl`)

---

## 🔌 Flask API Backend

**Tech:** Flask, `flask-cors`, scikit-learn, pandas, NumPy

**Endpoint:**
- `POST /api/predict_home_price`  
  Takes property features as input and returns predicted price.

**Start Server:**

```bash
cd client
python3 server.py
