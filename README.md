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
```

---

## 🌐 Web Frontend

**Directory:** `client/`

**Files:**
- `app.html`
- `app.js`
- `style.css`

**Features:**
- User input form (square footage, location, BHK, etc.)
- Fetches prediction from Flask API.

---

## ☁️ Deployment on AWS EC2

### A. Launch EC2 Instance

- Use Ubuntu
- Allow ports: `22 (SSH)` and `80 (HTTP)`

```bash
ssh -i "~/.ssh/YOUR-KEY.pem" ubuntu@YOUR-EC2-PUBLIC-DNS
```

Install NGINX:

```bash
sudo apt update
sudo apt install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
```

---

### B. Copy Code to Server

Using `scp`:

```bash
scp -i ~/.ssh/YOUR-KEY.pem -r Housing-Price-Prediction ubuntu@YOUR-EC2-PUBLIC-DNS:/home/ubuntu/
```

Or using Git:

```bash
git clone https://github.com/taranroyyuru/Housing-Price-Prediction.git
```

---

### C. Configure NGINX

Create config:

```bash
sudo nano /etc/nginx/sites-available/housing-price-prediction.conf
```

Paste the following:

```nginx
server {
    listen 80;
    server_name _;

    root /home/ubuntu/Housing-Price-Prediction/client;
    index app.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location /api/ {
        rewrite ^/api/(.*)$ /$1 break;
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable it:

```bash
sudo ln -s /etc/nginx/sites-available/housing-price-prediction.conf /etc/nginx/sites-enabled/
sudo unlink /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx
```

---

### D. Install Python Dependencies & Run App

```bash
sudo apt update
sudo apt install python3-pip
pip3 install flask flask-cors pandas numpy scikit-learn

cd /home/ubuntu/Housing-Price-Prediction/client
python3 server.py
```

---

## 🌍 Try the Deployed App

Visit:  
```
http://YOUR-EC2-PUBLIC-DNS/
```

Submit property details and receive real-time price predictions.

---

## 📁 Project Structure

```text
Housing-Price-Prediction/
├── client/
│   ├── app.html
│   ├── app.js
│   ├── style.css
│   └── server.py
├── server/
│   └── model.pkl
├── data/
│   └── [your training data]
├── requirements.txt
```

---

## 📝 Notes

- Update paths, usernames, and SSH keys to match your setup.
- This project follows real-world deployment best practices (NGINX as a reverse proxy).
- See source code for detailed documentation and comments.

---

**Built and maintained by [@taranroyyuru](https://github.com/taranroyyuru)**  
Enjoy predicting home prices on your own cloud! 🏠
