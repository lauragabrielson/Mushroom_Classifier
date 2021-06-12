# Now, scale the data and make a prediction ...

# 1. Create three diffferent sets of inputs (i.e., three
# different irises). Note that each set is constructed 
# as a list inside of another list (or an array inside of
# another array). This is how scikit-learn needs it. 
input_row1 = [[6.7, 3.0, 5.2]]
input_row2 = [[5.1, 3.5, 1.4]]
input_row3 = [[5.7, 2.8, 4.1]]

# 2. Transform each input using the scaler function.
input_row1_scaled = scaler.transform(input_row1)
input_row2_scaled = scaler.transform(input_row2)
input_row3_scaled = scaler.transform(input_row3)

# 3. Make a prediction for each input.
predict = randomforest.predict(input_row1_scaled)
print(f'Prediction 1 is: {predict_labels[predict[0]]}')

predict =randomforest.predict(input_row2_scaled)
print(f'Prediction 2 is: {predict_labels[predict[0]]}')

predict =randomforest.predict(input_row3_scaled)
print(f'Prediction 3 is: {predict_labels[predict[0]]}')
