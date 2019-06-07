M1 = [[12,7,3],
[4 ,5,6],
[7 ,8,9]]

M2 = [[5,8,1],
[6,7,3],
[4,5,9]]

sum = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

for i in range(len(M1)):
    for j in range(len(M1[0])):
        sum[i][j] = M1[i][j] + M2[i][j]
print(sum)

#scaler multiplication
X = [[12,7,3],
[4 ,5,6],
[7 ,8,9]]

Y = 9

sum1 = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

for i in range(len(X)):
    for j in range(len(X[0])):
        sum[i][j] = X[i][j] * Y
    
print(sum)

#multiplication of given matrix and vector
X = [[ 5, 1 ,3],
    [ 1, 1 ,1],
    [ 1, 2 ,1]]

Y = [[1, 2, 3]]

sum2 = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]
b = range(1)
for i in b:
    for j in range(len(X)):        
        X[i][j] = X[i][j] * Y[i][j]
print(X)

# Multiplication of Matrices
A = [[ 1, 1 ,1],
    [ 1, 1 ,1],
    [ 1, 1 ,1]]

B = [[ 1, 1 ,1],
    [ 1, 1 ,1],
    [ 1, 1 ,1]]


for i in range(len(A)):
    for j in range(len(A[0])):
        for k in range(len(A[0])):
            sum[j][k]=  sum[i][j] + ( A[j][k] * B[j][k])

print("Mul ",sum)



