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


##############
# Parameters #
##############

neurons = 1
epochs = 15
batch_size = 1
validation_size = 0.2


#####################
# Creating datasets #
#####################

dataset = pd.read_csv('dataset/dataset.csv')

x = dataset['input_x']
y = dataset['output_y']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=validation_size)


#################
# Training loop #
#################

model = Sequential([
    Dense(neurons, activation = 'linear',  input_dim = 1),
])

model.compile(optimizer = 'adam', loss = 'mean_squared_error')

model.fit(X_train, y_train, batch_size = batch_size, epochs = epochs)

# weight = 1, bias = 2
# The model multiplies the input by the weight (1) and adds the bias at the end (2), resulting in x+2 = y.
weights, bias = model.layers[0].get_weights()
print(f"Weights: {weights}, bias: {bias}")

predicts = model.predict(X_test)

precision = accuracy_score(y_test, predicts) * 100
print(f"Model accuracy: {precision}")