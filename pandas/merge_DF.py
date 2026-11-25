from operator import index

import pandas as pd
# df1=pd.DataFrame({"keys":["A","B","C","D"],"values":[1,2,3,4]})
# df2=pd.DataFrame({"keys":["A","B","C","D"],"values":[5,6,7,8]})
# print(df1,df2)

#inner join
# mrg1=pd.merge(df1,df2,on="keys")
# print(mrg1)
# df1=pd.DataFrame({"keys":["A","B","C","D"],"values":[1,2,3,4]})
# df2=pd.DataFrame({"keys":["B","C","D","E"],"values":[5,6,7,8]})
# mrg1=pd.merge(df1,df2,on="keys") # by default is inner join
# print(mrg1)
# parameeter of how
# mrg1=pd.merge(df1,df2,how="inner",on="keys")
# print(mrg1)

# lef outer join
# left_mrg1=pd.merge(df1,df2,how="left", on="keys")
# print(left_mrg1)

# right outer join
# right_mrg1=pd.merge(df1,df2,how="right", on="keys")
# print(right_mrg1)

# full outer join
# full_join=pd.merge(df1,df2,how="outer", on="keys")
# print(full_join)

# merge with multiple column
# df1=pd.DataFrame({"key1":["A","B","C","D"],"key2":[1,2,3,4],"values":[1,2,3,4]})
# df2=pd.DataFrame({"key1":["A","B","C","D"],"key2":[1,2,3,5],"values":[5,6,7,8]})
# mul_key_join=pd.merge(df1,df2,on=["key1","key2"])
# print(mul_key_join)

# merge with index
# df1=pd.DataFrame({"value1":[1,2,3]},index=["A","B","C"])
# df2=pd.DataFrame({"value1":[4,5,6]},index=["B","C","D"])
# mrg=pd.merge(df1,df2,left_index=True,right_index=True,how="outer")
# print(mrg)

# suffixes parameter
# df1=pd.DataFrame({"value1":[1,2,3]},index=["A","B","C"])
# df2=pd.DataFrame({"value1":[4,5,6]},index=["B","C","D"])
# mrg=pd.merge(df1,df2,left_index=True,right_index=True,suffixes=("python","id"),how="outer")
# print(mrg)

# coppy parameter
# df1=pd.DataFrame({"keys":["A","B","C","D"],"values":[1,2,3,4]})
# df2=pd.DataFrame({"keys":["B","C","D","E"],"values":[5,6,7,8]})
# mrg1=pd.merge(df1,df2,on="keys", copy=True)
# print(mrg1)

#sort parameter
# df1=pd.DataFrame({"keys":["A","B","C","D"],"values":[1,2,3,4]})
# df2=pd.DataFrame({"keys":["B","C","D","E"],"values":[5,6,7,8]})
# mrg1=pd.merge(df1,df2,on="keys", sort=False)
# print(mrg1)


