import pandas as pd

data = {
    "Name":["Hemanth","Ravi"],
    "Marks":[96,90]
}
df = pd.DataFrame(data)
'''print(df)
print(df.shape)
print(df.columns)
print(df.index)'''
#print(df["Name"])
#print(df[["Name","Marks"]])
print(df.loc[0:2])
df.iloc[0]

#df["Branch"] = ["CSM","CSD"]
#print(df[df["Marks"] > 90])

#print(df)