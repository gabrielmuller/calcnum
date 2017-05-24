import math

def big_F(i, x):
    if (i == 0):
        return x[0]*x[1] - 1
    elif (i == 1):
        return x[0] - math.exp(x[1])
print ("hey")
print (big_F(1, [1.1, 1.0]));
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

h = 0.1
error = 10e-5

xi = [1, 1]
iters = 6
small_j = [[0, 0], [0, 0]]
small_f = [0, 0]

for it in range(iters+1):
    
    for i in range(len(small_j)):
        for j in range(len(small_j[0])):
            xh = xi[:]
            xh[j] += h
            small_j[i][j] = (big_F(i, xh) - big_F(i, xi))/ h
                                  
    for i in range(len(small_f)):
        small_f[i] = -big_F(i, xi)

    sigma = gaussSolve(small_j, small_f)

    for i in range(len(xi)):
        xi[i] += sigma[i]
        
    print("Iter " + str(it) + ": " + str(xi))
