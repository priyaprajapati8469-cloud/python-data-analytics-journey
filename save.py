import pandas as pd
data = {
    "name":['ram','shayam','ghansham'],
    "age":[20,21,15],
    "city":['nagpur','pune','mumbai']
}
df=pd.DataFrame(data)
print(df)

# df.to_csv("output.csv",index=0)
# df.to_excel("column.xlsx",index=0)
df.to_json("new.json",index=False)


