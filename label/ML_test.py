import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Step 1: Load the new data
new_data = pd.read_csv('test2.txt')

# Step 2: Extract features and labels
features = new_data[['satellite_count', 'average_snr', 'satellite_change']]
labels = new_data['inside_outside']

# Step 3: Load the trained model
model = joblib.load('inside_outside_model2.pkl')

# Step 4: Make predictions
predictions = model.predict(features)

# Step 5: Evaluate the model
accuracy = accuracy_score(labels, predictions)
report = classification_report(labels, predictions)

print("Accuracy:", accuracy)
print("Classification Report:\n", report)