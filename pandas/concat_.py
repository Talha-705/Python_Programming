import pandas as pd
# concate of series
# s1=pd.Series([1,2,3,4,5])
# s2=pd.Series([11,22,33,44,55])
# con=pd.concat([s1,s2])
# print(con)

# concate of dataframes
# df1=pd.DataFrame({"key1":["A","B","C","D"],"values":[1,2,3,4]})
# df2=pd.DataFrame({"key1":["A","B","C","D"],"values":[5,6,7,8]})
# print(pd.concat([df1,df2]))

# axis parameter
# df1=pd.DataFrame({"key1":["A","B","C","D"],"values":[1,2,3,4]})
# df2=pd.DataFrame({"key1":["A","B","C","D"],"values":[5,6,7,8]})
# print(pd.concat([df1,df2],axis=1))

# join parameter
# df1=pd.DataFrame({"key1":["A","B","C","D"],"values":[1,2,3,4]})
# df2=pd.DataFrame({"key1":["A","B","C","D"],"values":[5,6,7,8]})
# print(pd.concat([df1,df2],join="inner")) #inner
# print(pd.concat([df1,df2],join="outer")) #outer

# key parameter
# df1=pd.DataFrame({"key1":["A","B","C","D"],"values":[1,2,3,4]})
# df2=pd.DataFrame({"key1":["A","B","D","E"],"values":[5,6,7,8]})
# print(pd.concat([df1,df2],axis=1,keys=["df1","df2"]))

#
