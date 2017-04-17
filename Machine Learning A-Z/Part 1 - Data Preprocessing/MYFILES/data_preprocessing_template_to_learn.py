# Data preprocessing

# Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values       #take all lines, take all colums except last -> take all values
y = dataset.iloc[:, 3].values
                
# Taking care of missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'median', axis = 0)  #consider "missing values" the values "NaN", substitute with the mean, axis = 0 for colums mean and axis = 1 for lines
imputer = imputer.fit(X[:, 1:3])     #apply imputer to the right colums: all lines, colums from 1 to 3 but 3 is EXCLUDED
X[:, 1:3] = imputer.transform(X[:, 1:3]) #really apply to the original selected matrix X

 # Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()                         #understanding how many different categories are in the columns
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0]) #creating an object to change the categorical colums 'country' --> making 0 or 1 values instead
X = onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()                         #understanding how many different categories are in the columns
y = labelencoder_y.fit_transform(y)

# Splitting the dataset into the Training Set and the Test Set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = scale.transform(X_test)