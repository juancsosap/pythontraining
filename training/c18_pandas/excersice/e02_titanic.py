import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

url = '../data/train.csv'

df = pd.read_csv(url)

print(df.head())