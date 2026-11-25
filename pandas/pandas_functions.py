import pandas as pd
#functions

csv2=pd.read_csv("D:\\pandas\\test_nwe5.csv", dtype={"a":"float"})
print(csv2)
#to find index of file
# print(csv2.index)

# to find columns in a file
# print(csv2.columns)

# describes function
# print(csv2.describe())

#head function
# print(csv2.head(2))

#tail function
# print(csv2.tail(2))

#to get specific rows
# print(csv2[:2])

# index in array
# print(csv2.index.array)

# csv to numpy
# print(csv2.to_numpy())

# convert into numpy array
# import numpy as np
# v=np.asarray(csv2)
# print(v)

# row index in dscending order
# print(csv2.sort_index(axis=0,ascending=False))

# column index in dscending order
# print(csv2.sort_index(axis=1,ascending=False))

# change column name with loc function
# csv2.loc[0,"a"]="python"
# print(csv2)

# use of loc to get data
# print(csv2.loc[[0,2],["a","b"]])

# iloc function
# print(csv2.iloc[3:2])

# drop() function
# print(csv2.drop("b",axis=1))

