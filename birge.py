a = [1, 0, 2, -1]
n = len(a)
b = [0]*n
c = [0]*(n-1)

b[0] = a[0]
c[0] = b[0]
iter = 2
x0 = 1
def itera(x0):
	for i in range(1, len(a)-1):
		b[i] = b[i-1]*x0 + a[i]
		c[i] = c[i-1]*x0 + b[i]
	b[n-1] = b[n-2]*x0 + a[n-1]

x = x0

for i in range (iter):
	itera(x)
	x = x - (b[n-1]/c[n-2])

print(x)
	
