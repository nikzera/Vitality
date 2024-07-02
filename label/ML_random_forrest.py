import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Step 1: Load and preprocess the data
data = pd.read_csv('output.txt')

# Step 2: Feature selection and label extraction
features = data[['satellite_count', 'average_snr', 'satellite_change']]
labels = data['inside_outside']

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# Step 4: Train a RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Step 5: Make predictions and evaluate the model
y_pred = clf.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model to disk (optional)
import joblib
joblib.dump(clf, 'inside_outside_model2.pkl')