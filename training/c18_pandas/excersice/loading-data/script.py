import numpy as np
import pandas as pd
import os

basedir = __file__[:__file__.rfind('/')+1]
if basedir != '': os.chdir(basedir)

logging_data = pd.read_csv('logging.csv', sep=';', header=None, names=['ID', 'Email', 'Password'])
users_data = pd.read_csv('users.csv', sep=',', header=None, names=['ID', 'Firstname', 'Lastname'])

print(logging_data)
print(users_data)

full_data = pd.merge(users_data, logging_data, on=['ID'], how='outer')
good_data = pd.merge(users_data, logging_data, on=['ID'], how='inner')

filter = full_data['ID'].isin(good_data['ID'])
columns = ['ID', 'Firstname', 'Email']
bad_data = full_data[~filter][columns]

print(bad_data)
