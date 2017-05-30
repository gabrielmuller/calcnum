import math

x = [2, 2.05, 2.10, 2.15]
y = [0.693, 0.718, 0.742, 0.765]
n = len(x)
def gaussSolve (a, b):
    n = len(a)
    for pivot in range(n-1):
        for line in range(pivot+1, n):
            factor = a[line][pivot] / a[pivot][pivot]
            for element in range(n):
                a[line][element] -= a[pivot][element] * factor
            b[line] -= b[pivot] * factor
            
    x = [0] * n
    for i in range(n):
        index = n - i - 1
        sum = b[index]
        for j in range(index+1, n):
            sum -= x[j] * a[index][j]
        x[index] = sum / a[index][index]
    
    return x
A = [[0 for x in range(n)] for y in range(n)]

for i in range(n):
    for j in range(n):
        A[i][j] = math.pow(x[i], j)



result = gaussSolve(A, y)
print (result)

