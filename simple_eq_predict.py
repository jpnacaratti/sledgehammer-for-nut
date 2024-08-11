#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 18:06:39 2024

@author: j.nacaratti
"""

from keras.layers import Dense
from keras.models import Sequential
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('dataset.csv')

x = dataset['input_x']
y = dataset['output_y']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

model = Sequential([
    Dense(1, activation = 'linear',  input_dim = 1),
])

model.compile(optimizer = 'adam', loss = 'mean_squared_error')

# 100% = batch_size = 1 e epochs = 15
model.fit(x_train, y_train, batch_size = 1, epochs = 15)

# weight = 1, bias = 2
# modelo multiplica a entrada pelo weight (1) e soma o bias no final (2) resultando em um x + 2 = y
weights, bias = model.layers[0].get_weights()

predicts = model.predict(x_test)

precision = accuracy_score(y_test, predicts) * 100

simple = model.predict((0,5))






