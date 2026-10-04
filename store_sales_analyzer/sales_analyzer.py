

import os

import pandas as pd


base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "sales.csv")

df = pd.read_csv(file_path)

print(df)