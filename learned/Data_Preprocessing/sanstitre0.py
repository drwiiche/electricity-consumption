# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:48:00 2020

@author: BRAHIM EL-MOUDEN
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')

x = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 3].values

#missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis= 0)
imputer = imputer.fit(x[:,1:3])

x[:,1:3] = imputer.transform(x[:,1:3])

#encoding categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
x[:,0] = labelencoder_x.fit_transform(x[:,0])
onehotencoder = OneHotEncoder(categorical_features = [0])
x = onehotencoder.fit_transform(x).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)