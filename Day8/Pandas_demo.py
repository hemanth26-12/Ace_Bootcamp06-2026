import pandas as pd

s = pd.Series([10,20,30,40])#1D

print(s)


df = pd.DataFrame({  #2D
    "Name":["Hemanth","Ravi","Krishna"],
    "Marks":[95,90,85]
})
print(df)