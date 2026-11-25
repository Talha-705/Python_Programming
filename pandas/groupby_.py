import pandas as pd
#  groupby function
df=pd.DataFrame({"name":["a","b","c","d","a","b","a","c","d","b","c"],
                 "s_1":[14,15,16,17,18,19,34,23,26,35,24],
                 "s_2":[32,23,34,44,21,22,33,43,54,64,12]})
# print(df)
df1=df.groupby("name")
for i,j in df1:
    print(i)
    print(j)
    print()

# to get data of a specific group
df2=df1.get_group("a")
print(df2)

# to find maximum nuber
print(df1.max())

# to find minimum nuber
print(df1.min())

# # to find  mean
print(df1.mean())

# conver DF in to list
print(list(df1))