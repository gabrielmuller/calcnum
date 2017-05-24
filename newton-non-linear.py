import math

def big_J(i, j, x):
    if (i == 0 and j == 0):
        return math.exp(x[0])
    elif (i == 0 and j == 1):
        return 1
    elif (i == 1 and j == 0):
        return 2*x[0]
    elif (i == 1 and j == 1):
        return 2*x[1]

def big_F(i, x):
    if (i == 0):
        return - (math.exp(x[0]) + x[1] - 1)
    elif (i == 1):
        return - (math.pow(x[0], 2) + math.pow(x[1], 2) - 4)
    
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
    
xi = [1, -1]
iters = 3
small_j = [[0, 0], [0, 0]]
small_f = [0, 0]

for it in range(iters):
    
    for i in range(len(small_j)):
        for j in range(len(small_j[0])):
            small_j[i][j] = big_J(i, j, xi)
                                  
    for i in range(len(small_f)):
        small_f[i] = big_F(i, xi)
    
    sigma = gaussSolve(small_j, small_f)

    for i in range(len(xi)):
        xi[i] += sigma[i]
        
    print("Iter " + str(it) + ": " + str(xi))
