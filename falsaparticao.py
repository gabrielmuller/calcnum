import math

def f(x):
  return math.pow(math.e, x)*math.sin(x) - 1
  
a = 0
b = 1
xm = 0
c = 0

while(abs(f(xm)) > 0.000001):
  c += 1
  xm = a - (f(a)*(b-a))/(f(b)-f(a))
  if (f(a)*f(xm) < 0):
    b = xm
  else:
    a = xm
  print(xm)
  
print("f(" + str(xm) + ") = 0")
print(str(c) + " iters")
