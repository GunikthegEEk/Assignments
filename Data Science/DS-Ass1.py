
''' Data Science Assignment
1. Input two 2-d list and convert it to ND Array. Multiply the nd arrays and display result. '''

import numpy as np 

Rsize = int(input("Enter the number of Rows:")) 
Csize = int(input("Enter the number of Columns:")) 
m1=[]
m2=[]
print("Enter Matrix-1 Data:")
for i in range(Rsize):          
    a =[] 
    for j in range(Csize):     
         a.append(int(input())) 
    m1.append(a) 
print("Enter Matrix-2 Data:")
for i in range(Rsize):         
    b =[] 
    for j in range(Csize):     
         b.append(int(input())) 
    m2.append(b) 

x=[m1,m2]
print("Matrices Data:")
for k in x:
    for i in range(Rsize): 
        for j in range(Csize): 
            print(k[i][j], end = " ") 
        print("")
    print("----")
#using numpy to convert lists & multiply matrices
matrix1 = np.array(m1)
matrix2 = np.array(m2)

#multiplying using np dot product 

res = np.dot(matrix1,matrix2) 
print("Multiplication Result (dot product):")
print(res)

#multiplying using @ operator
res = matrix1 @ matrix2 
print("Multiplication Result (@ operator):")
print(res)

'''
OUTPUT:
Enter the number of Rows:2
Enter the number of Columns:2
Enter Matrix-1 Data:
4
12
6
3
Enter Matrix-2 Data:
5
1
23
7
Matrices Data:
4 12
6 3
----
5 1
23 7
----
Multiplication Result (dot product):
[[296  88]
 [ 99  27]]
Multiplication Result (@ operator):
[[296  88]
 [ 99  27]]
'''