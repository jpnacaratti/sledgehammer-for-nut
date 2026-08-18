# A sledgehammer to crack a nut

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Keras](https://img.shields.io/badge/Keras-D00000?logo=keras&logoColor=white)](https://keras.io/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/jpnacaratti/sledgehammer-for-nut)](https://github.com/jpnacaratti/sledgehammer-for-nut/commits/develop/)

This repository contains code to build a Deep Learning model capable of solving a simple equation x + 2 = 7.

# Instructions
#### Requirements

Make a new virtualenv and install all the requirements from `requirements.txt` with the following command.
```
pip install -r requirements.txt
```
This project was written in Python 3.10.14 so I cannot guarantee it works on any other version.

#### Data
The dataset used to train the model can be found in the path: `dataset/dataset.csv`.
You can easily generate a new one run by running `simple_eq_dataset.py` script.

#### Train yourself
To crack a nut using a sledgehammer and train your model, you can simply run the `simple_eq_predict.py` script.
```
python simple_eq_predict.py
```
