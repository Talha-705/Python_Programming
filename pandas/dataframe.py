import pandas as pd
#llist to  DF
l=[1,2,8,3,4,5,6]
df=pd.DataFrame(l)
print(df)
print(type(df))
# dictionary to DF
dic={"Name":['talha','ali','umar'],"rol":[1,2,3],"cgpa":[2.3,4.7,4.6]}
df=pd.DataFrame(dic)
print(df)
# to get  specific column from dictionary
dic={"Name":['talha','ali','umar'],"rol":[1,2,3],"cgpa":[2.3,4.7,4.6]}
df=pd.DataFrame(dic,columns=["rol","Name"])
print(df)

# to get specific value from DF
print(df['Name'][1])

# list to DF
l=[[1,2,3,4,5],[21,22,23,24,25,26]]
df=pd.DataFrame(l)
print(df)

# DF from two sseries
s={"v":pd.Series([1,2,3,4,5]), "v1":pd.Series([14,24,24,35,35])}
print(s)
df=pd.DataFrame(s)
print(df)

# update
df.at[0,'v']=67
print (df)

# arithmatic operations
# #for sum
var=pd.DataFrame({"a":[1,2,3,4,5],"b":[9,8,7,6,5]})
print(var)
var["c"]=var["a"]+var["b"]
print(var)

# #for sub
var=pd.DataFrame({"a":[1,2,3,4,5],"b":[9,8,7,6,5]})
print(var)
var["c"]=var["a"]-var["b"]
print(var)

# #for mul
var=pd.DataFrame({"a":[1,2,3,4,5],"b":[9,8,7,6,5]})
print(var)
var["c"]=var["a"]*var["b"]
print(var)

# #for div
var=pd.DataFrame({"a":[1,2,3,4,5],"b":[9,8,7,6,5]})
print(var)
var["c"]=var["a"]/var["b"]
print(var)

#logical operator
var=pd.DataFrame({"a":[5,10,15,20,25],"b":[9,8,27,16,5]})
var["python"]=var["a"]>=20
print(var)

# insertion
var=pd.DataFrame({"a":[1,2,3,4,5],"b":[9,8,7,6,5]})
var.insert(1,"new",var["a"])
print(var)
#or
var=pd.DataFrame({"a":[1,2,3,4,5],"b":[9,8,7,6,5]})
var.insert(2 ,"new",[2,4,6,8,20])
print(var)

#deletation
var1=var.pop("new")
print(var)

# rettrive specific value ffrom DF
DF=pd.DataFrame({"a":[5,10,15,20,25],"b":[9,8,27,16,5]})
DF["python"]=DF["a"][:2]
print(DF)

DF=pd.DataFrame({"a":[5,10,15,20,25],"b":[9,8,27,16,5]})
DF["python"]=DF["a"][2:4]
print(DF)

# CSV to XlS
# df=pd.DataFrame({"a":[5,10,15,20,25],"b":[9,8,27,16,5]})
# df.to_csv("test_nwe2.csv")
# #remove indexes
# df=pd.DataFrame({"a":[5,10,15,20,25],"b":[9,8,27,16,5]})
# df.to_csv("test_nwe1.csv", index=False)
# # change columns name in xls
# df=pd.DataFrame({"a":[5,10,15,20,25],"b":[9,8,27,16,5]})
# df.to_csv("test_nwe3.csv", index=False,header=["Banana","mango"])
#
# # read csv file
# csv=pd.read_csv("D:\\pandas\\test_nwe2.csv ")
# print(csv)
#
#
# csv1=pd.read_csv("D\\pandas\\test_nwe2.csv ")
# print(csv1)