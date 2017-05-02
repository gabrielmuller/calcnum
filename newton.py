
import math

def f(x):
  return math.pow(math.e, x) - x - 1

def df(x):
  return math.pow(math.e, x) - 1
a = 0
b = 1
xm = 0.5
c = 0

while(abs(f(xm)) > 0.000001):
  c += 1
  xm = xm - (f(xm) / df(xm))
  print(xm)

print("f(" + str(xm) + ") = " + str(f(xm)))
print(str(c) + " iters")
