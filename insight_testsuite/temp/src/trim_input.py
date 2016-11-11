import pandas as pd
import os

cur_path = os.path.dirname('__file__')

input_path = os.path.relpath('..\\paymo_input\\batch_payment.csv', cur_path)


data = pd.read_csv(input_path, usecols=[1, 2])
