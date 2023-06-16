##  i x k : k x j == i x j


A = [[1, 5, 3],  ## 3 x 3
    [4, 0, 2],
    [6, 0, 3]]

B = [[1, 0],   ## 3 x 2
    [1, 0], 
    [5, 0]]

# A(3 x 3) : B(3 x 2) --->  C(3 x 2)

C = [[0, 0],  # initializing empty matrix
    [0, 0],   ## len(C) == no. of rows
    [0, 0]]   ## len(C[0]) == no. of columns
# print(len(C))
# print(len(C[0]))

for i in range(0, len(C)):
    for j in range(0, len(C[0])):
        for k in range(0, len(B)):
            C[i][j] += A[i][k] * B[k][j]

# print(C)

for row in C :
    print(row)
    
# for column in C:
#     print(column)




