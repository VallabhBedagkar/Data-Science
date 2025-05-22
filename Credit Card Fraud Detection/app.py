from flask import Flask, request, jsonify,render_template
import pickle
import numpy as np
import json

app = Flask(__name__)

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('predict_form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        raw_input = request.form['features']
        features = [float(x.strip()) for x in raw_input.split(',')]
        input_array = np.array([features])  # reshape for model
        prediction = model.predict(input_array)[0]

        result = "❌ Fraudulent Transaction" if prediction == 1 else "✅ Legitimate Transaction"
        return render_template('predict_form.html', prediction_text=result)
    except Exception as e:
        return render_template('predict_form.html', prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)
