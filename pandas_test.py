import pandas as pd
df1 = pd.DataFrame({
"Company Name":["Google", "Microsoft", "SpaceX","Amazon","Samsung"],
"Founders":['Larry Page','Bill Gates','Elon Musk','Jeff Bezos', 'Lee Byungchul'],
"Founded": [1998, 1975, 2002, 1994, 1938],
"Number of Employees": [103459, 144106, 6500647,50320,67145]})
df2 = pd.DataFrame({
'Company Name':['WhatsApp'],
'Founders':['Jan Koum, Brian Acton'],
'Founded': [2009],
'Number of Employees': [5000]}, index=['i'])
res = df1.append(df2,ignore_index = True)
print(res)
data = res
"""
data = res.drop([res.index[5]])
data = res[res.Founders != 'Bill Gates']
"""
print(data)
print(data.columns)
print(data.dtypes)

print(data.shape) # printing rows & columns
print(data.shape[0]) # to print rows
print(data.shape[1]) # to print column

print(data.head())
print(data.head(2))

print(data.tail())
print(data.tail(1))

print(data[0:4])
print(data[3:])
print(data[:4])
print(data[data['Number of Employees'] > 10000][['Company Name', 'Founders', 'Founded', 'Number of Employees']])
print(data[data.Founded > 2000][['Company Name', 'Founders', 'Founded', 'Number of Employees']])
print(data.iloc[2,3])
print(data.iloc[1,2])

print(data.at[3,'Founders'])

print(data.iat[1,1])
print(data.iat[2,2])
