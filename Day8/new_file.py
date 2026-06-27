import pandas as pd

df = pd.read_csv("Day8/naruto.csv", encoding="cp1252")
#rint(df.info)
#print(df)
#print(df.loc[210:220][df["Year_launch"] > 2010])
#df.set_index("Title",inplace= True)
#print(df.loc[180:190],["Year_launch"])
#df.reset_index(inplace=True)
#rint(df.loc[210:220][df["Year_launch"] > 2010])
#filt = (df["Saga"]=="The Gathering of the Five kage")
#print(df.loc[filt].sort_index(ascending=True).head())
flit=df["Year_launch"] > 2011 & (df["Saga"]=="The Gathering of the Five kage")
print(df.loc[flit])