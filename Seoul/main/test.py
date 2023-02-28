import pandas as pd
import numpy as np
from sklearn.datasets._base import load_csv_data

filepath = "../log/logfile3.log"

df = pd.read_csv(filepath, sep="|")
df = str(df).replace("[", "")
df = str(df).replace("]", "")
df = str(df).replace("'", "")


print(df)