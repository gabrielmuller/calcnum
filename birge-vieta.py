a = [1, 0, 2, -1]
n = len(a)
b = [0] * n
c = [0] * (n - 1) 

numIts = 10
counter = 0

xi = 1
xold = 0

def ruffini (x, y, r):
    y[0] = x[0]
    for i in range(1, len(y)):
        y[i] = x[i] + y[i-1] * r;

while (counter < numIts):
    ruffini(a, b, xi);
    print(b)
    ruffini(b, c, xi);

    xold = xi
    xi -= (b[n-1] / c[n-2])
    
    counter += 1
    print("Iter " + str(counter) + ": " + str(xi))
    
