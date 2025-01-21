# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load your data
# Replace 'your_data.csv' with the path to your dataset
df = pd.read_excel(r'Cleaned_data.xlsx')

# Define the features and target variable
features = ['Temperature', 'Humidity', 'Wind_Speed', 'Cloud_Cover', 'Pressure']
X = df[features]
y = df['Rain']  # Target variable for rain prediction

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Example prediction
example_data = [[25,80,10,81,1012]]  # Replace with actual data for prediction
predicted_rain = model.predict(example_data)
print("Predicted Rain (1=Yes, 0=No):", predicted_rain[0])
