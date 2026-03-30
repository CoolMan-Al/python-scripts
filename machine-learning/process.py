#!/usr/bin/env python

# If not using the google thingy, run "pip install scikit-learn pandas"
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the data
data = pd.read_csv("loan_risk_prediction_dataset.csv")
# Details about the data 
data.head()
data.info()
data.describe()
# Check for empty values (THere is)
data.isnull().sum()
# Index for columns with integers/floats
num_cols = data.select_dtypes(include=['int64', 'float64']).columns
# Fill fields in numerical columns with medians of that column
data[num_cols] = data[num_cols].fillna(data[num_cols].median())
# Extrapolates string fields into boolean fields (City > City_Houston,New York, San Fransisco)
data = pd.get_dummies(data, drop_first=True)
# Ensure no empty values remain
data.isnull().sum()
# Remove result column
X = data.drop('LoanApproved', axis=1)
# Store result column in seperate variable
y = data['LoanApproved']

# Sampling Data (Taking random parts of it)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Create a blank model
model = RandomForestClassifier(n_estimators=100, random_state=42)
# Train model off of data
model.fit(X_train,y_train)
# Test the model on the test set
y_pred = model.predict(X_test)

pdb.set_trace()
