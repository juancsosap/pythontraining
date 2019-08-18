import pandas as pd


url = 'http://bit.ly/uforeports'
data = pd.read_csv(url)

condition = (data['Shape Reported'] == 'SPHERE')
filtered_data = data[condition]

sortered_data = filtered_data.sort_values('Time', ascending=False)

result_data = sortered_data.drop('Shape Reported', axis=1)

result_data.rename(columns={'Colors Reported': 'Color'}, inplace=True)

print(result_data.head())
