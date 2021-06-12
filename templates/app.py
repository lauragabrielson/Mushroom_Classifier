# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
from pickle import load

# Initialize the flask App
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Load the model from its pickle file. (This pickle 
# file was originally saved by the code that trained 
# the model. See mlmodel.py)
randomforest = load(open('rf_mushrooms.pkl', 'rb'))

# Load the scaler from its pickle file. (This pickle
# file was originally saved by the code that trained 
# the model. See mlmodel.py)
scaler = load(open('scaler.pkl','rb'))

# Define the index route
@app.route('/')
def home():
    return render_template('index.html')

# Define a route that runs when the user clicks the Predict button in the web-app
@app.route('/predict',methods=['POST'])
def predict():
    
    # Create a list of the output labels.
    prediction_labels = ['Edible', 'Poisonous']
    
    # Read the list of user-entered values from the website. Note that these
    # will be strings. 
    features = [x for x in request.form.values()]

    # Convert each value to a float.
    float_features = [float(x) for x in features]

    # Put the list of floats into another list, to make scikit-learn happy. 
    # (This is how scikit-learn wants the data formatted. We touched on this
    # in class.)
    final_features = [np.array(float_features)]
     
    # Preprocess the input using the ORIGINAL (unpickled) scaler.
    # This scaler was fit to the TRAINING set when we trained the 
    # model, and we must use that same scaler for our prediction 
    # or we won't get accurate results. 
    final_features_scaled = scaler.transform(final_features)

    # Use the scaled values to make the prediction. 
    prediction_encoded = randomforest.predict(final_features_scaled)
    prediction = prediction_labels[prediction_encoded[0]]

    # Render a template that shows the result.
    prediction_text = f'Mushroom type is predicted to be :  {prediction}'
    return render_template('index.html', prediction_text=prediction_text, features=features)


# Allow the Flask app to launch from the command line
if __name__ == "__main__":
    app.run(debug=True)