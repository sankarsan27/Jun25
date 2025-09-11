import sys
print(sys.executable)
import pandas as pd
print('check2')
import snowflake_uuid
print("check4")
print("check5")
print("chck6")



import numpy as np
class Kmeans_SG():
    def __init__(self,df,k,max_iter=None,tol=1e-4):
        self.data=df
        self.k=k
        self.tol=tol
        self.max_iter=max_iter

    def standardize(self):
        self.data=(self.data-self.data.mean())/self.data.std()
        self.data=(self.data-self.data.min())/(self.data.max()-self.data.min())

    

        
import pandas as pd
dataset=pd.DataFrame({'age':[23,34,56,21,67,35,33,26,78,33,57,74,46],'income':[1000,2100,1567,7663,2356,3678,1765,1452,2076,4327,4321,1456,3214]})
dataset


f=Kmeans_SG(dataset,5)

f.standardize()
f.data

##adding some comments
