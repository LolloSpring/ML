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
from sklearn.preprocessing import LabelEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])