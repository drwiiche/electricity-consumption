# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:25:19 2020

@author: BRAHIM EL-MOUDEN
"""

#Importing the libraries
import numpy as np
import pandas as pd

#importing the dateset

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,0]