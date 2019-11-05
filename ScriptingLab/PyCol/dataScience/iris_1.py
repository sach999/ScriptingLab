import pandas as pd
from pandas import Series, DataFrame

#Series - 1D Array

# get titanic & test csv files as a pandas DataFrame
iris_df = pd.read_csv("iris.csv") #Loads data to memory, irist_df is a dataStructure
print("......Printing the IRIS DataFrame completely.....")
print(iris_df)
print(".............Printing the Info.....")
iris_df.info()
print("........Describing.....")
iris_df.describe()

