
import math

def f(x):
  return math.pow(x, 2) - 5

def df(x):
  return 2*x

xm = 2
c = 0

while(abs(f(xm)) > 1e-3):
  c += 1
  xm = xm - (f(xm) / df(xm))
  print(xm)

print("f(" + str(xm) + ") = " + str(f(xm)))
print(str(c) + " iters")
