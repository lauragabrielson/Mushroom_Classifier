# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
from pickle import load
from tensorflow.keras.models import load_model


# Initialize the flask App
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Load the model from its pickle file. (This pickle 
# file was originally saved by the code that trained 
# the model. See mlmodel.py)
# mushroom_model = joblib.load('knn_standard_three.pkl')
from tensorflow.keras.models import load_model
mushroom_model = load_model("app_mushroom_trained.h5")

# # Load the scaler from its pickle file. (This pickle
# # file was originally saved by the code that trained 
# # the model. See mlmodel.py)
mushroom_scaler = load(open('mush_nn_scale.pkl','rb'))

# Define the index route
@app.route('/')
def home():
    return render_template('index.html')

# Define a route that runs when the user clicks the Predict button in the web-app
# Many thanks to Farshad and Dom for the initial code to create this prediction function!
# As well as the help in adjusting it to work with a neural network
@app.route('/predict',methods=['POST'])
def predict():
    
    # Python code to convert string to list

    cap_color = request.form.get('cap_colors')
    cap_shape = request.form.get('cap_shapes')
    cap_surface = request.form.get('cap_surfaces')
    
    print(cap_color)
    print(cap_shape)
    print(cap_surface)

    return cap_shape

    # def Convert(string):
    #     li = list(string.split(","))
    #     return li

    # # Create a list of the output labels.
    # prediction_labels = ['Edible', 'Poisonous']
    
    # # Read the list of user-entered values from the website. Note that these
    # # will be strings. 
    # features = [x for x in request.form.values()]

    # # Ok this is where we add all the additional features
    
    # # Read the value selected for cap surface
    # cap_surface = request.form.getlist('cap_surfaces')
    # # Convert string to float
    # cap_surface = Convert('teststring') # THIS WORKED update the repo to have strings as the source value then proceed   
    # # Extend feature with array from cap surface value
    # features.extend(cap_surface)

    # # Read the value selected for cap color
    # cap_color = request.form.getlist('cap_colors')
    # # Extend feature with array from cap color value
    # features.extend(cap_color)

    #  # Read the value selected for bruises_bleed
    # bruise_bleed = request.form.getlist('bruise_bleed')
    # # Extend feature with array from bruise_bleed value
    # features.extend(bruise_bleed)

    #  # Read the value selected for gill attachments
    # gill_attachment = request.form.getlist('gill_attachments')
    # # Extend feature with array from cap color value
    # features.extend(gill_attachment)

    #  # Read the value selected for gill spacing
    # gill_spacing = request.form.getlist('gill_spacing')
    # # Extend feature with array from gill spacing value
    # features.extend(gill_spacing)

    #  # Read the value selected for gill color
    # gill_color = request.form.getlist('gill_colors')
    # # Extend feature with array from gill color value
    # features.extend(gill_color)

    #  # Read the value selected for cap shape
    # cap_shape = request.form.getlist('cap_shapes')
    # # Extend feature with array from cap shape value
    # features.extend(cap_shape)

    #  # Read the value selected for stem color
    # stem_color = request.form.getlist('stem_colors')
    # # Extend feature with array from stem color value
    # features.extend(stem_color)

    #  # Read the value selected for has_ring
    # has_ring = request.form.getlist('has_ring')
    # # Extend feature with array from has_ringvalue
    # features.extend(has_ring)

    #  # Read the value selected for ring_type
    # ring_type = request.form.getlist('ring_types')
    # # Extend feature with array from ring type value
    # features.extend(ring_type)

    #  # Read the value selected for habitat
    # habitat = request.form.getlist('habitats')
    # # Extend feature with array from habitat value
    # features.extend(habitat)

    # # Read the value selected for seasons
    # season = request.form.getlist('seasons')
    # # Extend feature with array from season value
    # features.extend(season)

    # # Convert each value to a float.
    # float_features = [float(x) for x in features]

    # # Put the list of floats into another list, to make scikit-learn happy. 
    # # (This is how scikit-learn wants the data formatted. We touched on this
    # # in class.)
    # final_features = [np.array(float_features)]
     
    # # Preprocess the input using the ORIGINAL (unpickled) scaler.
    # # This scaler was fit to the TRAINING set when we trained the 
    # # model, and we must use that same scaler for our prediction 
    # # or we won't get accurate results. 
    # final_features_scaled = mushroom_scaler.transform(final_features)

    # # Use the scaled values to make the prediction. 
    # prediction_encoded = mushroom_model.predict(final_features_scaled)
    # # prediction = prediction_labels.values

    # # Render a template that shows the result.
    # prediction_text = f'Mushroom is predicted to be :  {prediction_encoded}'
    # return render_template('index.html', prediction_text=prediction_text, features=features)


# Allow the Flask app to launch from the command line
if __name__ == "__main__":
    app.run(debug=True)