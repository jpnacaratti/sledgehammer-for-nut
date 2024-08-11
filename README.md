# A sledgehammer to crack a nut

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
