
import math

def f(x):
  return math.pow(x, 2) - 5

xm = 0
xm_old = 2
c = 0
fxm = f(xm)

while(abs(fxm) > 1e-3):
  c += 1

  xm_new = xm - ((fxm * (xm - xm_old)) / (fxm - f(xm_old)))
  xm_old = xm
  xm = xm_new

  fxm = f(xm) #otimiza
  print(xm)

print("f(" + str(xm) + ") = " + str(f(xm)))
print(str(c) + " iters")
