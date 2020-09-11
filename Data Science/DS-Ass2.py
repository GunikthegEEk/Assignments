''' Data Science Assignment
2. Make a dataset, which has features of type nominal, ordinal, interval, ratio and categorical. Add atleast 5 rows. Convert it to numeric data '''

#Creating a Dataset using Pandas 
import pandas as pd
import numpy as np
from pandas import DataFrame

#Creating DataFrame

info = {'Name': ['Gunik','Jaineet','Gaurav','Ayush','Jog'], #Nominal
        'Age': [21,21,19,24,20], #Categorical
        'Grade' : ["BCA","BBA","12th","M.Tech","B.Com"], #Categorical
        'PUBG BAN Reaction': ["Satisfied","Dissatisfied ","Very Dissatisfied","Indifferent","Very Dissatisfied"], #Ordinal
        'IG Survival Time(mins)': [7,18,22,10,4], #Interval
        'Avg. Daily Time Spent Playing(hours)': [1,2,3,0.5,2] #Ratio
        }

df = DataFrame(info, columns= 
['Name', 
'Age',
'Grade',
'PUBG BAN Reaction',
'IG Survival Time(mins)',
'Avg. Daily Time Spent Playing(hours)'])


print('DataFrame\n----------\n', df)
print('\nDataFrame Datatypes:\n', df.dtypes)

#convert pandas dataframe to numpy array (numeric data)
arr = df.to_numpy()

print('\nNumpy Array\n----------\n', arr)
print('\nNumpy Array Datatype :', arr.dtype)

'''
OUTPUT:

DataFrame
----------
       Name  Age   Grade  PUBG BAN Reaction  IG Survival Time(mins)  Avg. Daily Time Spent Playing(hours)
0    Gunik   21     BCA          Satisfied                       7                                   1.0
1  Jaineet   21     BBA      Dissatisfied                       18                                   2.0
2   Gaurav   19    12th  Very Dissatisfied                      22                                   3.0
3    Ayush   24  M.Tech        Indifferent                      10                                   0.5
4      Jog   20   B.Com  Very Dissatisfied                       4                                   2.0

DataFrame datatypes :
 Name                                     object
Age                                       int64
Grade                                    object
PUBG BAN Reaction                        object
IG Survival Time(mins)                    int64
Avg. Daily Time Spent Playing(hours)    float64
dtype: object

Numpy Array
----------
 [['Gunik' 21 'BCA' 'Satisfied' 7 1.0]
 ['Jaineet' 21 'BBA' 'Dissatisfied ' 18 2.0]
 ['Gaurav' 19 '12th' 'Very Dissatisfied' 22 3.0]
 ['Ayush' 24 'M.Tech' 'Indifferent' 10 0.5]
 ['Jog' 20 'B.Com' 'Very Dissatisfied' 4 2.0]]

Numpy Array Datatype : object

'''