# Mushroom Classifier
## Using Machine Learning to Classify Mushrooms as Edible or Poisonous.
#### University of Minnesota Data Visualization & Analysis Boot Camp
Laura Gabrielson, Beau Jeffrey, Melissa Lowe, Stephanie Richards


For this project, we used a dataset from The Mushroom Project (https://mushroom.mathematik.uni-marburg.de/) by Dennis Wagner, Dominik Heider, and Georges Hattab at Philipps Universitat in Marburg, Germany.  We chose this dataset based on European species because it contains the most comprehensive data on mushroom attributes and was created for machine learning tasks.

We then followed the same steps outlined in the European dataset to create a new simulated dataset based on North American species.  We combined these datasets in order to train our model to correctly classify both European and North American mushroom species.

We evaluated several different maching learning models to classify our dataset including random forest, decision tree, k-nearest neighbors and neural network.

This repo contains everthing necessary to recreate our project. Please follow the instructions listed below to run our machine learning models, display our findings and make a prediction. 

## Instructions
1. Clone repo.
1. Open a Terminal/Gitbash on the root folder (Mushroom_Classifier)
1. Type ```source activate PythonData``` and press the enter key to activate the Python environment.
1. Type ```jupyter notebook``` launch the Jupyter Notebook.
1. Open the *.ipynb* files.
1. Run all of the cells in the *.ipynb* files.
1. In your Terminal/Gitbash, type ```python app.py``` and hit enter to run the Flask app.
1. [Click this link](http://127.0.0.1:5000/) or open a web browser--preferrably Google Chrome--and type ```http://127.0.0.1:5000/``` into the url bar. Hit enter.

## How to Recreate the North American data
1. Open a Terminal/Gitbash window on the "NA_data_generation" folder.
1. Type ```source activate PythonData```.
1. Type ```python secondary_data_gen.py```. **WARNING**: Running this file will overwrite "north_american_secondary_data_generate.csv" and "north_american_secondary_data_shuffled.csv".
1. From this point, you can run the "North_American_Mushrooms_secondary_data.ipynb" file. You will be able to run it up to cell 76. This cell will export a .csv file that will need to be shuffled before work can continue.
1. In your Terminal/Bash window, type ```python shuffle_data.py```. **WARNING**: Running this file will overwrite "all_mushroom_data_shuffled.csv".
1. Continue in the Jupyter Notebook until the end. This will dump pickled scaler and model files for the Random Forest model, using two outputs.
1. To create the machine learning models with four outputs, open and run the Jupyter Notebook called "four_output_machine_learning" through cell 8. In your Terminal/Bash window, run ```python four_output_shuffle.py```. Continue in the Jupyter Notebook until the end. Use the pickled scaler and model for the Random Forest type to import into app.py in the root directory.

## Guide to Navigating the Website:

The website displays the characteristics of our datasets and also uses Random Forest to make a live prediction based on 15 different mushroom attributes. When the page initially loads, you will see an accordian layout with various sections that are expandable. Click on an individual section to navigate between the following sections: 'Introduction', 'Explore the Data' or 'Make a Prediction'. To explore the data, click on the side buttons to view the different attributes of our datasets. If you would like to make a prediction, enter attributes of a specific mushroom species for each section - cap, gills, stem, ring and other and click on the 'Submit' button to see the prediction.