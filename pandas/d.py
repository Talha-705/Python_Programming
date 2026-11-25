import pandas as pd
# CSV to XlS
# df=pd.DataFrame({"a":[5,10,15,20,25],"b":[9,8,27,16,5]})
# df.to_csv("test_nwe5.csv")
# #remove indexes
# df=pd.DataFrame({"a":[5,10,15,20,25],"b":[9,8,27,16,5]})
# df.to_csv("test_nwe5.csv", index=False)
# # change columns name in xls
# df=pd.DataFrame({"a":[5,10,15,20,25],"b":[9,8,27,16,5]})
# df.to_csv("test_nwe3.csv", index=False,header=["Banana","mango"])
#
# # read csv file
# csv=pd.read_csv("D:\\pandas\\test_nwe2.csv")
# print(csv)
#
# # # to read a specific row
# csv1=pd.read_csv("D\\pandas\\test_nwe2.csv")
# print(csv1)
#
# # to read a specific columns
# csv1=pd.read_csv("D\\pandas\\test_nwe2.csv", usecols=["a"])
# print(csv1)
#
# # to skip secific row
#
# csv1=pd.read_csv("D\\pandas\\test_nwe2.csv", skiprows=[0,3])
# print(csv1)
#
# # make column to index
# # to read a specific row
# csv1=pd.read_csv("D\\pandas\\test_nwe2.csv", index_col="b")
# print(csv1)

# to make row as header
# csv2=pd.read_csv("D:\\pandas\\test_nwe5.csv", header=2)
# print(csv2)

# given name as headings
# csv2=pd.read_csv("D:\\pandas\\test_nwe5.csv", names=["col1","col2"])
# print(csv2)

# to remove headings
# csv2=pd.read_csv("D:\\pandas\\test_nwe5.csv", header=None)
# print(csv2)

# to change datatype of a column
# csv2=pd.read_csv("D:\\pandas\\test_nwe5.csv", dtype={"a":"float"})
# print(csv2)



