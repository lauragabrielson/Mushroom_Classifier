# Import libraries
import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib
from pickle import load
from tensorflow.keras.models import load_model
# from sklearn.preprocessing import LabelEncoder, MinMaxScaler
# from tensorflow.keras.utils import to_categorical


# Initialize the flask App
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Load the model from its pickle file. (This pickle 
# file was originally saved by the code that trained 
# the model. See mlmodel.py)
mushroom_model = joblib.load('combined_data_rf_model.pkl')
# from tensorflow.keras.models import load_model
# mushroom_model = load_model("app_mushroom_trained.h5")

# # Load the scaler from its pickle file. (This pickle
# # file was originally saved by the code that trained 
# # the model. See mlmodel.py)
# mushroom_scaler = load(open('mush_nn_scale.pkl','rb'))
mushroom_scaler = load(open('combined_data_scaler.pkl','rb'))

# Define the index route
@app.route('/')
def home():
    return render_template('index.html')

# Define a route that runs when the user clicks the Predict button in the web-app
# Many thanks to Farshad and Dom for the initial code to create this prediction function!
# As well as the help in adjusting it to work with a neural network
@app.route('/predict',methods=['POST'])
def predict():

    # Create a list of the output labels.
    prediction_labels = ['Edible', 'Poisonous']

    # Create lists to hold quantitative qualitative data
    quantitative = []
    qualitative = []

    # Create list to compile all inputs
    all_input = []
    
    # Read quantitative input fields
    # Convert to floats
    diameter = request.form.get('cap_diameter')
    height = request.form.get('stem_height')
    width = request.form.get('stem_width')

    # Add diameter, width, and height to quantitative list
    quantitative.append(diameter)
    quantitative.append(height)
    quantitative.append(width)

    # Convert quantitative items to float and append to all input
    for i in range(0, len(quantitative)):
        quantitative[i] = float(quantitative[i])
        all_input.append(quantitative[i])

    # Read qualitative input fields
    
    # # Old attempt here for reference for the moment
    # # Read the value selected for cap surface
    # cap_surface = request.form.getlist('cap_surfaces')
    # # Convert string to float
    # cap_surface = Convert('teststring') # THIS WORKED update the repo to have strings as the source value then proceed   
    # # Extend feature with array from cap surface value
    # features.extend(cap_surface)


    # Read the value selected for cap surface
    cap_surface = request.form.get('cap_surfaces')
    
    # Convert string post into list
    cap_surface = cap_surface.split(",")

    # Convert list string data types into integers
    for i in range(0, len(cap_surface)):
        cap_surface[i] = int(cap_surface[i])
        qualitative.append(cap_surface[i])

    # Read the value selected for cap color
    cap_color = request.form.get('cap_colors')
    
    # Convert string post into list
    cap_color = cap_color.split(",")

    # Convert list string data types into integers
    for i in range(0, len(cap_color)):
        cap_color[i] = int(cap_color[i])
        qualitative.append(cap_color[i])

    # Read the value selected for bruises_bleed
    bruise_bleed = request.form.get('bruise_bleed')
   
    # Convert string post into list
    bruise_bleed = bruise_bleed.split(",")

    # Convert list string data types into integers
    for i in range(0, len(bruise_bleed)):
        bruise_bleed[i] = int(bruise_bleed[i])
        qualitative.append(bruise_bleed[i])

    # Read the value selected for gill attachments
    gill_attachment = request.form.get('gill_attachments')
    
    # Convert string post into list
    gill_attachment = gill_attachment.split(",")

    # Convert list string data types into integers
    for i in range(0, len(gill_attachment)):
        gill_attachment[i] = int(gill_attachment[i])
        qualitative.append(gill_attachment[i])

    # Read the value selected for gill spacing
    gill_spacing = request.form.get('gill_spacings')

    # Convert string post into list
    gill_spacing = gill_spacing.split(",")

    # Convert list string data types into integers
    for i in range(0, len(gill_spacing)):
        gill_spacing[i] = int(gill_spacing[i])
        qualitative.append(gill_spacing[i])

    # Read the value selected for gill color
    gill_color = request.form.get('gill_colors')
    
    # Convert string post into list
    gill_color = gill_color.split(",")

    # Convert list string data types into integers
    for i in range(0, len(gill_color)):
        gill_color[i] = int(gill_color[i])
        qualitative.append(gill_color[i])

    # Read the value selected for cap shape
    cap_shape = request.form.get('cap_shapes')
    
    # Convert string post into list
    cap_shape = cap_shape.split(",")

    # Convert list string data types into integers
    for i in range(0, len(cap_shape)):
        cap_shape[i] = int(cap_shape[i])
        qualitative.append(cap_shape[i])    

    # Read the value selected for stem color
    stem_color = request.form.get('stem_colors')
    
    # Convert string post into list
    stem_color = stem_color.split(",")

    # Convert list string data types into integers
    for i in range(0, len(stem_color)):
        stem_color[i] = int(stem_color[i])
        qualitative.append(stem_color[i])

    # Read the value selected for has_ring
    has_ring = request.form.get('has_ring')
    
    # Convert string post into list
    has_ring = has_ring.split(",")

    # Convert list string data types into integers
    for i in range(0, len(has_ring)):
        has_ring[i] = int(has_ring[i])
        qualitative.append(has_ring[i])

    # Read the value selected for ring_type
    ring_type = request.form.get('ring_types')
    
    # Convert string post into list
    ring_type = ring_type.split(",")

    # Convert list string data types into integers
    for i in range(0, len(ring_type)):
        ring_type[i] = int(ring_type[i])
        qualitative.append(ring_type[i])

    # Read the value selected for habitat
    habitat = request.form.get('habitats')
    
    # Convert string post into list
    habitat = habitat.split(",")

    # Convert list string data types into integers
    for i in range(0, len(habitat)):
        habitat[i] = int(habitat[i])
        qualitative.append(habitat[i])

    # Read the value selected for seasons
    season = request.form.get('seasons')
    
    # Convert string post into list
    season = season.split(",")

    # Convert list string data types into integers
    for i in range(0, len(season)):
        season[i] = int(season[i])
        qualitative.append(season[i])

    # THIS SHOULD ONLY HAPPEN AT THE END OF ALL QUALITATIVE COLLECTION 
    # MOVE THIS AS YOU WORK THROUGH ALL FIELDS
    # OTHERWISE IT WILL DUPLICATE AND TRIPLICATE AND HORRIFICALLY MANGLE EVERYTHING
    for i in qualitative:
        all_input.append(i)

    # Convert each value to a float.
    float_input = [float(x) for x in all_input]

    # Put the list of floats into another list, to make scikit-learn happy. 
    # (This is how scikit-learn wants the data formatted. We touched on this
    # in class.)
    final_input = [np.array(float_input)]
     
    # Preprocess the input using the ORIGINAL (unpickled) scaler.
    # Look into this note
    # This scaler was fit to the TRAINING set when we trained the 
    # model, and we must use that same scaler for our prediction 
    # or we won't get accurate results. 
    final_input_scaled = mushroom_scaler.transform(final_input)

    # # Let's try the scaler in a different way
    # final_scaled = mushroom_scaler.transform(all_input)

    # Use the scaled values to make the prediction. 
    prediction_encoded = mushroom_model.predict(final_input_scaled)
    prediction = prediction_labels[prediction_encoded[0]]

    # Render a template that shows the result.
    prediction_text = f'Mushroom is predicted to be :  {prediction}'
    return render_template('index.html', prediction_text=prediction_text)


# Allow the Flask app to launch from the command line
if __name__ == "__main__":
    app.run(debug=True)