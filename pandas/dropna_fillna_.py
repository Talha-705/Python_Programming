#dropna and fillna

import pandas as pd
# pddf=pd.DataFrame({"name":["Talha","Ali","umar","Ahad","Asjad","sami","hadi","rehman","bilal","luqman","shaoib","fazal"],
#     "roll":[1,2,3,4,5,6,7,8,9,10,11,12],
#     "City":["fsd","lhr","","multan","dgk","","lhr","skp","fsd","lhr","","dik"],
#     "cgpa":[3.65,3.22,2.2,5,4,1.8,1.0,3.2,3.76,3.9,2.87,2.16],
#     "Status":["p","p","f","","p","p","f","f","p","","f","p"]})
# print(df)
# df.to_csv("text9.csv")
# csv4=pd.read_csv("D:\\pandas\\text9.csv")
# print(csv4)

# dropna function
# dropna function is used to remove row columns in which data is missing
# print(csv4.dropna())

#rempove row
# print(csv4.dropna(axis=0))

#rempove column
# print(csv4.dropna(axis=1))

csv5=pd.read_csv("D:\\pandas\\text8.csv")
# print(csv5)
# to remove in row all is nill values
# print(csv5.dropna(how="all"))
#or
# print(csv5.dropna(how="any"))

# to rem ove null valus of a particular colmn
# print(csv5.dropna(subset=["City"]))
#or
# print(csv5.dropna(subset=["City","Status"]))

#inplace parameter : remove all nulls
# print(csv5.dropna(inplace=True))
 # thresh parameter :
# print(csv5.dropna(thresh=2))

#fillna()
# print(csv5.fillna("python"))

#diff values in diff columns
# print(csv5.fillna({"City":"python","Status":"hy"}))

#methods parameter
# print(csv5.fillna(method="ffill", axis=0)) #ffill: used for forward filling data
# print(csv5.fillna(method="bfill")) #ffill: used for backword filling data

# inplace parameter
# print(csv5.fillna(12,inplace=True))

# limit parameter
# print(csv5.fillna("python",limit=1))

# REPLACE AND INTERPOLATE
# replace()
# print(csv5.replace(to_replace=5,value=22))
#or
# print(csv5.replace(to_replace="Ali",value="khubaib"))

# print(csv5.replace([2,3,4,5,7,9],44))

# regex parametter
# print(csv5.replace("[A-Z]","python",regex=True))
# print(csv5.replace("[A-Za-z]","python",regex=True))

# use of dictionary
# print(csv5.replace({"name":"[A-Z]"},"python",regex=True))

#methods parameter
# print(csv5.replace("lhr",method="bfill"))

# limit
# print(csv5.replace("lhr",method="bfill",limit=2))

#inplcae parameter
# print(csv5.replace("lhr",method="bfill",limit=2, inplace=True))

# INTERPOLATE () Function
# print(csv5.interpolate()) # work on digit directly
#methods
# print(csv5.interpolate(method="linear", axis=0))
# llimit
# print(csv5.interpolate(limit=2))

#limit directions
# print(csv5.interpolate(limit_direction="forward",limit=2)) #for forword dirrection
# print(csv5.interpolate(limit_direction="backward",limit=1)) #for backworddirrection
# print(csv5.interpolate(limit_direction="both",limit=2)) #for both dirrection