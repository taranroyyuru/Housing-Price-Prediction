Housing Price Prediction
This project demonstrates the end-to-end pipeline for building, deploying, and serving a Machine Learning-powered real estate price prediction website using a custom dataset. It features a data science workflow, a Flask backend, a modern HTML/JS frontend, and deployment to AWS EC2 using NGINX.

Project Overview
Goal: Predict home prices using regression and serve predictions through a web interface.

Components:

Data preprocessing and model building (Python, pandas, numpy, scikit-learn)

REST API backend (Flask)

Web frontend (HTML, CSS, JavaScript)

Production deployment (Ubuntu, AWS EC2, NGINX)

GitHub repository: taranroyyuru/Housing-Price-Prediction

1. Data Science & Model Training
Dataset: Custom or public real estate price dataset (e.g., Bangalore Home Prices from Kaggle)

Steps:

Data Ingestion & Cleaning (pandas, numpy)

Outlier Detection & Removal

Feature Engineering, Dimensionality Reduction

Train/Test Split, GridSearchCV, K-fold Cross Validation

Model Persistence: save best model as model.pkl or similar

2. Flask API Backend
Directory: /Users/taranroyyuru/Housing Price Prediction/client/server.py

Tech: Flask, flask-cors, scikit-learn, pandas, numpy

Endpoints:

/api/predict_home_price (POST): Takes features, returns price prediction.

Example start command:
bash
python3 "/Users/taranroyyuru/Housing Price Prediction/client/server.py"
3. Web Frontend
Directory: /Users/taranroyyuru/Housing Price Prediction/client/

Files: app.html, app.js, style.css

Features:

User form for square footage, bedrooms, location, etc.

Fetches prediction from Flask API.

4. Deployment Instructions (AWS EC2 Example)
A. Prepare EC2
Launch Ubuntu EC2 instance, set security group to allow ports 22 (SSH) and 80 (HTTP).

SSH into instance:

bash
ssh -i "~/.ssh/YOUR-KEY.pem" ubuntu@YOUR-EC2-PUBLIC-DNS
Update and install NGINX:

bash
sudo apt update
sudo apt install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
B. Copy Code to Server
Using scp:

bash
scp -i ~/.ssh/YOUR-KEY.pem -r "/Users/taranroyyuru/Housing Price Prediction" ubuntu@YOUR-EC2-PUBLIC-DNS:/home/ubuntu/
Or, using git:

bash
git clone https://github.com/taranroyyuru/Housing-Price-Prediction.git
C. NGINX Setup
Create config:

bash
sudo nano /etc/nginx/sites-available/housing-price-prediction.conf
Sample contents:

text
server {
    listen 80;
    server_name _;
    root "/home/ubuntu/Housing Price Prediction/client";
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
Enable config and reload NGINX:

bash
sudo ln -s /etc/nginx/sites-available/housing-price-prediction.conf /etc/nginx/sites-enabled/
sudo unlink /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx
D. Install Python Dependencies & Start Flask
bash
sudo apt update
sudo apt install python3-pip python3-flask python3-numpy python3-scikit-learn
cd "/home/ubuntu/Housing Price Prediction/client"
python3 server.py
5. Try Your Deployed App
Open a browser and navigate to http://YOUR-EC2-PUBLIC-DNS/

Submit details and obtain real-time predictions directly from the deployed ML model.

6. Project Structure
text
Housing Price Prediction/
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
7. Notes
Update paths/usernames/keys as needed for your own cloud/server setup.

This workflow follows real-life production deployment best practices with NGINX reverse-proxying Flask.

See code for detailed documentation and comments.

Built and maintained by taranroyyuru. Enjoy predicting home prices on your own cloud!
