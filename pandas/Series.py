import pandas as pd


a=[1,2,4,5]
series=pd.Series(a)
print(series)
# type
print(type(series))
# extract values
print(series[2])
# change index
c=pd.Series(a,index=['a','s','d','f'])
print(c)
# change datatype
c=pd.Series(a,index=['a','s','d','f'], dtype="float")
print(c)
# gaven name to series
c=pd.Series(a,index=['a','s','d','f'], dtype="float", name="python")
print(c)
# dictionary to series
dic={"Name":['talha','ali','umar'],"rol":[1,2,3],"cgpa":[2.3,4.7,4.6]}
s=pd.Series(dic)
print(s)

v=pd.Series(12)
print(v)

# for same but more values

v=pd.Series(12,index=[1,2,3,4,5,5,8,67,7])
print(v)

# addup to 2 series
v1=pd.Series(16,index=[1,2,3,4,5,5,8,67,7])
v=pd.Series(12,index=[1,8,67,7])
print(v+v1)