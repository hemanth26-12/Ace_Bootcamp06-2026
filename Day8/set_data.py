import pandas as pd

data = {
    "Name" : ["Hemanth","Vasudev","Dinesh","Chaithanya","Aravind","Prateek"],
    "Roll_No" : [24,49,"Le-7",44,46,28],
    "Branch" : ["CSM","CSD","CSE","CSO","CSO","CSM"]
    
}

df = (pd.DataFrame(data,index=[1,2,3,4,5,6]))
#print(df)
print(df.loc[(2,5),["Branch","Name"]])
