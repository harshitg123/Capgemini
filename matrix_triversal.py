import math

matrix = [[1,2,3,4], 
          [5,6,7,8], 
          [9,10,11,12], 
          [13,14,15,16]
          ]

rows = len(matrix)
columns = len(matrix[0])

i=0
j=0
n=0
R = rows
C = columns
count =0

if rows == columns:
    n = rows/2
elif rows > columns:
    n = math.ceil(columns/2)
else:
    n = math.ceil(rows/2)

while(count < n):

    while(j < columns-1):
        print(matrix[i][j], end=" ")
        j = j+1
    
    while(i < rows -1):
        print(matrix[i][j], end=" ")
        i = i+1
    
    while(j > columns-C):
        print(matrix[i][j], end=" ")
        j = j-1

    while(i > rows-R):
        print(matrix[i][j], end=" ")
        i = i-1

    i = i+1
    j = j+1
    C = C -1
    R = R -1
    count = count+1

'''
 Logic for solving the question

                               ij ij ij ij

                               00 01 02 03 --> First while loop.
                               10 11 12 13
                               20 21 22 23
     Third while loop      <-- 30 31 32 33
                                         |
                                         V
                                         Second while loop

Like wise fourth one is printing from 11, 12, ....

'''