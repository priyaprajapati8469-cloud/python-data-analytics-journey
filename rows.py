#head()  tail()
# head()-prints first 5 rows  head(10)-print first 10 rows
#tail()-prints last 5 rows  head(10)-print last 10 rows
import pandas as pd
data={
    "rollno":[101,102,103,104,105],
    "Name":['priya','pragya','nabu','gyanu','sourabh'],
    "age":[20,25,22,23,19],
    "marks":[99,84,40,99,60]
}
df=pd.read_json("sample_Data.json")

# print("display first 5 rows:\n",df.head())
# print("display last 5 rows:\n",df.tail())

# df=pd.DataFrame(data)
# print(df)

# print("descriptive statistic:")
# print(df.describe())

# print(f'shape:{df.shape}')
# print(f'column:{df.columns}')


#[]-to select colums for filtering 
#boolean condition-to select rows for filtering 

#selectind single columns
# print("Name (single columns return series)")
# # print(df["Name"])
#      #or
# name=df['Name']  
# print(name)   

# # #selcting multiple columns
# # print("subset with name and marks:\n")
# subset=df[["Name","marks"]]
# print(subset)

#single condition
# high_salary=df[df['marks']>80]
# print("student with more than 80 marks")
# print(high_salary)

#multiple condition
# filtered=df[(df['age']>=22) & (df['marks']>85)]
# print(filtered)

# filtered_OR=df[(df['age']>=22) | (df['marks']>85)]
# print(filtered_OR)

# print("display the information of dataset")
# print(df.info())

# print("descriptive statistic:")
# print(df.describe())


  


