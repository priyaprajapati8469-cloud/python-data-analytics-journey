# import pandas as pd
# data={
#     "ID":[,101,102,103,104,105],
#     "Name":["sahu",'priya','pragya','nabu','gyanu','sourabh'],
#     "age":[None,20,25,22,23,19],
#     "salary":[None,5000,7500,7000,4000,9000]
# }

# df=pd.DataFrame(data)
# # print(df)

#square barcket synatx-df["column_name"]=some_data
# df["Bonus"] = df['salary']*0.1     #10% increment in marks
# print(df)

# using insert() method-add  new column at any position
#synatx-df.insert(loc,"column name",[some data])
# df.insert(2,"city",['pune','hydrabad','UP','gkp','blr'])
# df.insert(3,"joining",[2022,2023,2026,2024,2021])
# print(df)

#updating single values
#.loc
#synatx-df.loc[row_index,"column row"]=new-values
# df.loc[3,"salary"]=10000
# print(df)

#updating existing column values
#increasing salary by 5%
# df["salary"]=df["salary"]*1.05
# print(df)


#removing single columns
# syntax-df.drop(columns=["column name"],inplace=True)
# df.drop(columns=["age"],inplace=True)
# print(df)

#removing multiple columns
# df.drop(columns=["age","ID"],inplace=True)
# print(df)


#identify missing values
# print(df.isnull())     #true-missing values   false-no missing values
# print(df.isnull().sum())   #count the nimber of missing values


# handling missing values(commom issues)
#NaN (not a number)
#None(for object data type)
#remove missing values-dropna()
# df.dropna(inplace=True)    #axis=0-remove row values ,axis=1-remove columns
# print(df)


#filling missing values-fillna()-mean,median,mode
#synatx-fillna(values,inplace=True)
# df.fillna(0,inplace=True)  #wrong
# print(df)

# df['age'] = df['age'].fillna(df['age'].mean())
# df['salary'] = df['salary'].fillna(df['salary'].mean())
# print(df)



# data={
#     "time":[1,2,3,4,5],
#     "value":[10,None,30,None,50]
# }
# df=pd.DataFrame(data)
# print("before interploation")
# print(df)

#intrepolate()-linear,polynomial,time
#syntax-df.interpolate(mathod="linear",axis,inplace)
# df['value']=df['value'].interpolate(method="linear")
# print("after interpolate")
# print(df)


#sorting and aggregation
#sorting data 1 column-sort_values()
# syantax-df.sort_values(by="column Name",True/False,inplace=True)       asc-True  Des-False

# import pandas as pd
# data={
#     "ID":[100,101,102,103,104,105],
#     "Name":['ashmita','priya','pragya','nabu','gyanu','sourabh'],
#     "age":[21,20,25,22,23,19],
#     "salary":[6000,5000,7500,7000,4000,9000]
# }

# df=pd.DataFrame(data)
# print(df)

#sorting and aggregation
#sorting data 1 column-sort_values()
# syantax-df.sort_values(by="column Name",True/False,inplace=True)       asc-True  Des-False

#sort single column
# df.sort_values(by="Name",ascending=True,inplace=True)
# df.sort_values(by="age",ascending=True,inplace=True)
# print(df)

#sorting multiple columns
# df.sort_values(by=["age","salary"],ascending=[True,False],inplace=True)
# print("descending  sorting")
# print(df)

# aggregation-involve calculating summary statistic(sum(),mean(),count(),min(),max(),std())
# synatx-df["column Name"].mean()/sum()/min()/max()
# min_sal=df["salary"].min()
# print("minimum salary is:",min_sal)
# max_age=df["age"].max()
# print("highest age is :",max_age)


# import pandas as pd
# data={
#     "ID":[100,101,102,103,104,105],
#     "Name":['ashmita','priya','pragya','nabu','gyanu','sourabh'],
#     "age":[22,20,25,22,19,19],
#     "salary":[6000,5000,7500,7000,4000,9000]
# }

# df=pd.DataFrame(data)
# print(df)
# #grouping in single column
# # group=df.groupby("age")["salary"].sum()
# # print(group)

# #grouping in  multiple column
# group=df.groupby(["age","Name"])["salary"].sum()
# print(group)

  #merging-cross,inner,outer,left,right
#syntax-pd.merge(df1,df2,on="column name",how="types of join")
import pandas as pd
#customer dataframe
customer_1=pd.DataFrame({
    'customer ID':[1,2,3],
    'name':['ramesh','suresh','sahil']
})

customer_2=pd.DataFrame({
    'customer ID':[1,2,4],
    'orderAmount':[250,123,160]
})
# merge=pd.merge(customer_1,customer_2,on="customer ID",how="inner")    
# print('cross joins',merge)    #-only matching keys will be printed
# merge=pd.merge(customer_1,customer_2,on="customer ID",how="left") 
# print('left joins',merge)
# merge=pd.merge(customer_1,customer_2,on="customer ID",how="right") 
# print('right joins',merge)
# merge=pd.merge(customer_1,customer_2,on="customer ID",how="inner") 
# print('inner joins',merge)
# merge=pd.merge(customer_1,customer_2,on="customer ID",how="outer") 
# print('outer joins',merge)

#concatenation-combining dataset either horizontal(column wise) or vertically(row wise)
pd.concat([customer_1,customer_2],axis=0,ignore_index=True)
[customer_1,customer_2]
axis=1
ignore_indx=True

#vertically
df_region1=pd.DataFrame({
    'customerID':[1,2],
    'Name':['raju','kaju']
})

df_region2=pd.DataFrame({
    'customerID':[3,4],
    'Name':['ram','sham']
})
#convatenate vertically
df_concat=pd.concat([df_region1,df_region2],ignore_index=True)
print(df_concat)

#concat horizontally
df_concat=pd.concat([df_region1,df_region2],axis=1,ignore_index=True)
print(df_concat)