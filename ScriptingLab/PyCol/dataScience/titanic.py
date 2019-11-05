'''
a) Load the titanic dataset into one of the data structures - numpy or pandas

b) convert the survived column to strings for easier readings
#Convert the class column to strings for easier reading
#Convert the Embarked column to strings for easier reading

c)Fill the empty column of Embarked with 'S'
#Fill the empty column of Cabin with 'XXX'

d)Drop the columns 'Parch', 'PassengerID', 'Name', 'Ticket', 'Embarked'
#Understand the meaning of axis = 1 and inplace = True or False

e) Display header rows and description of the laoded dataset.
'''

import numpy as np
import pandas as pd


#a)
titanic_df = pd.read_csv('dataSet/titanictrain.csv') #opening a file

#print(titanic_df.head(5)) .head(5) prints the first 5 rows of the dataSet 

#c)
titanic_df ['Survived'] = titanic_df ['Survived'].map({
    0: 'Died',
    1:'Survived'
})

titanic_df ['Pclass'] = titanic_df ['Pclass'].map({
    1:'Luxury',
    2:'Business',
    3:'Basic'
})

#d)
titanic_df.drop(['Parch', 'PassengerId', 'Name', 'Ticket'], axis=1, inplace = False)
#inpalce - drop from reference
titanic_df['Embarked'] = titanic_df['Embarked'].fillna('S')
print(titanic_df.head(5))
