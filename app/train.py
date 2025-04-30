import numpy as np
import pandas as pd

df = pd.read_csv('data/train.csv')
# print(df.head())
mean_age = df['Age'].mean()
median_fare = df['Fare'].median()