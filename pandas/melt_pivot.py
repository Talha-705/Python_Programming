import pandas as pd
# melt() function
df=pd.DataFrame({"days":[1,2,3,4,5,6],"urdu":[13,14,15,25,14,24],"english":[11,21,43,11,53,34]})
# print(pd.melt(df)) # for vertically reshape

# to make cols as id
print(pd.melt(df, id_vars=["days"]))  #id_vars

# change name of variable
print(pd.melt(df, id_vars=["days"], var_name="python")) # var_name

# change name of value
print(pd.melt(df, id_vars=["days"], value_name="price")) # value_name

# piovt() function
df=pd.DataFrame({"days":[1,2,3,4,5,6],"name":['a','b','b','a','b','b'],
                 "urdu":[13,14,15,25,14,24],"english":[11,21,43,11,53,34]})
print(df.pivot(index="days",columns="name")) # pivot

 # to get data of specific column
print(df.pivot(index="days",columns="name",values="english"))

# for perform matahmetically fun on table
df=pd.DataFrame({"days":[1,1,1,1,2,2,],"name":['a','b','b','a','b','b'],
                 "urdu":[13,14,15,25,14,24],"english":[11,21,43,11,53,34]})
print(df.pivot_table(index="name",columns="days",aggfunc="mean")) # mean
print(df.pivot_table(index="name",columns="days",aggfunc="max")) # max
print(df.pivot_table(index="name",columns="days",aggfunc="sum")) # sum

# margins parameter
# used to find average values
print(df.pivot_table(index="name",columns="days",aggfunc="mean", margins=True)) # margins=True