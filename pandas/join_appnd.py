import pandas as pd
# join function
# df1=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
# df2=pd.DataFrame({"C":[21,22,23,24,25],"D":[31,32,33,44,55]})
# print(df1.join(df2))


# df1=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
# df2=pd.DataFrame({"C":[21,22,23],"D":[31,32,33]})
# print(df1.join(df2))

#index parameter
# df1=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]},index=['a','b','c','d','e'])
# df2=pd.DataFrame({"C":[21,22,23],"D":[31,32,33]}, index=['a','b','c'])
# print(df1.join(df2))

# df1=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]},index=['a','b','c','d','e'])
# df2=pd.DataFrame({"C":[21,22,23],"D":[31,32,33]})
# print(df1.join(df2))

# how parameter
# df1=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
# df2=pd.DataFrame({"C":[21,22,23],"D":[31,32,33]})
# df3=df1.join(df2, how="inner") # inner
# print(df3)
# df3=df1.join(df2, how="outer") # outer
# print(df3)
# df3=df1.join(df2, how="left") # left
# print(df3)
# df3=df1.join(df2, how="right") #right
# print(df3)
# df3=df1.join(df2, how="cross") # cross
# print(df3)

#suffix parameter
# df1=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
# df2=pd.DataFrame({"C":[21,22,23],"B":[31,32,33]})
# print(df1.join(df2,lsuffix="_13",rsuffix="_13"))


# append function
df1=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
df2=pd.DataFrame({"C":[21,22,23],"B":[31,32,33]})
# print(df1._append(df2))

## to maintain sequenced
# print(df1._append(df2,ignore_index=True))

df1=pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
df2=pd.DataFrame({"C":[21,22,23],"D":[31,32,33]})
print(df1._append(df2))