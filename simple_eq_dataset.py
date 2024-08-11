#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 17:46:18 2024

@author: j.nacaratti
"""

import pandas as pd
import numpy as np


#################
# Configuration #
#################

num_rows = 15000
lower_range = 0
higher_range = 1000


###################
# Generating loop #
###################

dataset = pd.DataFrame(columns=['input_x', 'output_y'])

for index in range(num_rows):
    print(f"Index: {index}")
    
    random_int = np.random.randint(lower_range, higher_range)
    
    tempDf = pd.DataFrame({
        'input_x': [random_int],
        'output_y': [(random_int + 2)]
    })
    
    dataset = pd.concat([dataset, tempDf], ignore_index = True)

dataset.to_csv('dataset/dataset.csv', index = False)
