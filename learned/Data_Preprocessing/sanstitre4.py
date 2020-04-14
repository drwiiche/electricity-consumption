# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:11:27 2020

@author: BRAHIM EL-MOUDEN
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#load dataset 

dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

#handling missing data

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)

imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

#encoding categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
x[:,0] = labelencoder_x.fit_transform(x[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0])
x = onehotencoder.fit_transform(x).toarray()

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
y


# splitting the dataset 

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# features scaling 

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_x
X_train = sc_x.fit_transform(X_train)
X_train