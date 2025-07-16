from flask import Flask, request, jsonify
from flask_cors import CORS  # Import Flask-CORS
import util

app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5001"])
 # Enable CORS for the entire app

# util will contain all the core routines while the server
# will just do request and response

# first routine is to return the location in banglore city
# IN UI application we want drop down that shows all the locations
@app.route('/get_location_names')
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    # CORS headers now automatically handled by Flask-CORS
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = (request.form['location'])
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    # simply call util.get estimated price where we are passing the params
    # and return the price
    # use postman
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    # CORS headers handled by Flask-CORS, no manual addition needed
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
