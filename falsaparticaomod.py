
import math

def f(x):
  return math.pow(math.e, x)*math.sin(x) - 1

a = 0
b = 1
xm = 0
c = 0
fa = f(a)
fb = f(b)
fxm = f(xm)
pa = 0
pb = 0
while(abs(f(xm)) > 0.000001):
  c += 1
  xm = a - (fa*(b-a))/(fb-fa)
  fxm = f(xm)
  if (fa*fxm < 0):
    pa = fb/(fb+fxm)
    b = xm
    fb = fxm
    fa = pa*fa
  else:
    pb = fa/(fa+fxm)
    fb = pb*fb
    a = xm
    fa = fxm
  print(xm)

print("f(" + str(xm) + ") = 0")
print(str(c) + " iters")
