# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:46:30 2021

@author: Ovindu Wijethunge
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

df = pd.read_csv('csvData.csv')
X = df.iloc[:, 1:-1].values
y = df.iloc[:, -1].values

from sklearn.neighbors import KNeighborsClassifier
dt = KNeighborsClassifier(n_neighbors=5)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
from sklearn.metrics import classification_report, confusion_matrix
from imblearn.over_sampling import RandomOverSampler
os =  RandomOverSampler()
from imblearn.combine import SMOTETomek
from imblearn.under_sampling import NearMiss 
smk = SMOTETomek(random_state=42)

X_res, y_res = smk.fit_sample(X, y)
X_train_res, X_test_res, y_train_res, y_test_res = train_test_split(X_res, y_res, test_size=0.30)
scaler.fit(X_train_res)
X_train_res = scaler.transform(X_train_res)
X_test_res = scaler.transform(X_test_res)
dt.fit(X_train_res, y_train_res)
y_pred = dt.predict(X_test_res)
print(confusion_matrix(y_test_res, y_pred))
print(classification_report(y_test_res, y_pred))

# Saving model to disk
pickle.dump(dt, open('model.pkl','wb'))

#x = [-0.501935,-0.0559087,-0.0161989,-0.297034,-0.601665,-0.235129,-0.267696,-0.372999,-0.622836,-0.407599,1.26674,-0.58052,-0.328634]
#y = [2.18214,-0.813473,-0.453712,-0.370705,-0.609161,-0.356038,-0.37072,-0.37333,-0.614514,-0.405674,-0.880783,-0.585333,-0.32857]
#z= [3.13797	0.526758	0.718818	-0.366098	-0.605731	-0.359687	-0.372008	-0.382341	3.51721	-0.417615	-0.871202	-0.588703	-0.329404]

# Loading model to compare the results
#model = pickle.load(open('model.pkl','rb'))
#print(model.predict([x,y]))