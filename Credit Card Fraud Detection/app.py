from flask import Flask, request, jsonify
import pickle
import numpy as np
import json

app = Flask(__name__)

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "Credit Card Fraud Detection API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = data.get('features', None)

    if features is None:
        return jsonify({'error': 'No features provided'}), 400

    features_np = np.array(features).reshape(1, -1)
    prediction = model.predict(features_np)[0]

    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
