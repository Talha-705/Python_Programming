import pandas as pd
import numpy as np
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

#chaking missing values
d = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}
df = pd.DataFrame(d)
mv = df.isnull()
print(mv)

# 1 filtring
d = pd.read_csv("D:\\pandas\\text8.csv")
bool_series = pd.isnull(d["Status"])
missing_data = d[bool_series]
print(missing_data)

# 2. Checking for Non-Missing Values Using notnull()
# Example 1: Identifying Non-Missing Values in a DataFrame
mv = df.notnull()
print(mv)

# Example 2: Filtering Data with Non-Missing Values
d = pd.read_csv("D:\\pandas\\text8.csv")
bool_series = pd.notnull(d["Status"])
missing_data = d[bool_series]
print(missing_data)

# datetime function
df = ['2021-01-01', '2020-05-22', '2022-03-15', '2021-07-30', '2020-11-11']
print(pd.to_datetime(df))

# Create a String Dataframe using Pandas
import pandas as pd
import numpy as np
data = {'Names': ['Gulshan', 'Shashank', 'Bablu', 'Abhishek', 'Anand', np.nan, 'Pratap'],
        'City': ['Delhi', 'Mumbai', 'Kolkata', 'Delhi', 'Chennai', 'Bangalore', 'Hyderabad']}
df = pd.DataFrame(data)
print(df)

# changing column ddata type
print(df.astype('string'))

# string manipulation
#  in lower form
print(df['Names'].str.lower())
#  in upper form
print(df['Names'].str.upper())
#  in strip
print(df['Names'].str.strip())
# split function
#  split()
print(df['Names'].str.split('a'))
# len()
print(df['Names'].str.len())
# cat(sep='')
print("\nafter using cat:")
print(df['Names'].str.cat(sep=', '))
# get_dummies()
print(df['City'].str.get_dummies())

# startswith()
print(df)
print(df['Names'].str.startswith('G'))

#endswith()
print(df['Names'].str.endswith('k'))

#replacea,b)
print(df['Names'].str.replace("Gulshan","khuram"))

# #repeate(value)
# print(df['Names'].str.repeat(2))

#count(patern)
print(df['Names'].str.count('a'))
#find
print(df['Names'].str.find('a'))
#findall\
print(df['Names'].str.findall('a'))
# islower
print(df['Names'].str.islower())
# is upper
print(df['Names'].str.isupper())
# is numeric
print(df['Names'].str.isnumeric())
# swapcase
print(df['Names'].str.swapcase())