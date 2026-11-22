"""
PW2 Lab B Part 2 -- three routes to a minimum.

Compare gradient descent, Newton, and SLSQP on two functions:
  2A: f(x) = (x-3)**2 + 1          (easy, one minimum at x=3)
  2B: g(x) = x**4 - 3*x**2 + x + 5 (harder, several stationary points)
Run:  python warmup.py
"""
import numpy as np
from scipy.optimize import newton, minimize

# ---------- 2A: easy convex function ----------
def f(x):   return (x-3)**2 + 1
def df(x):  return 2*(x-3)
def d2f(x): return 2.0

# TODO 2A: minimise f three ways from x0=0 and print each result:

print("For f(x) = (x-3)**2 + 1:")
print("\tx0 = 0\n")

#   (1) gradient descent by hand (loop x = x - lr*df(x) until the step is tiny)
x = 0
lr = 0.1
iterations = 100
for i in range(iterations):
    x = x - lr*df(x)

print("\tGradient descent minimum: x =", x, ";\ty =", f(x))

#   (2) scipy.optimize.newton(df, x0, fprime=d2f)
x0 = 0
newtonMin = newton(df, x0, fprime=d2f)

print("\tNewton's method minimum: x =", newtonMin, ";\ty =", f(newtonMin))

#   (3) scipy.optimize.minimize(f, x0, method="SLSQP")
x0 = 0
slsqpMin = minimize(f, x0, method="SLSQP")

print("\tSLSQP minimum: x =", slsqpMin.x[0], ";\ty =", f(slsqpMin.x[0]))


# ---------- 2B: harder landscape ----------
def g(x):   return x**4 - 3*x**2 + x + 5
def dg(x):  return 4*x**3 - 6*x + 1
def d2g(x): return 12*x**2 - 6

# TODO 2B: run the same three methods on g, from x0=0 AND from x0=2.

print("\nFor g(x) = x**4 - 3*x**2 + x + 5")

# x0 = 0
print("\tx0 = 0:\n")

#   (1) gradient descent:
x = 0
lr = 0.1
iterations = 100
for i in range(iterations):
    x = x - lr*dg(x)

print("\tGradient descent minimum: x =", x, ";\ty =", g(x))

#   (2) Newton method
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
x0 = 0
newtonMin = newton(dg, x0, fprime=d2g)

sign = d2g(newtonMin)
print("\tNewton's method", ("minimum" if sign > 0 else "maximum" if sign < 0 else "flat point") + ": x =", newtonMin, ";\ty =", g(newtonMin))

#   (3) SLSQP Method
x0 = 0
slsqpMin = minimize(g, x0, method="SLSQP")

print("\tSLSQP minimum: x =", slsqpMin.x[0], ";\ty =", g(slsqpMin.x[0]))

# x0 = 2
print("\n\n\tx0 = 2:\n")

#   (1) gradient descent:
x = 2
lr = 0.1
iterations = 100
for i in range(iterations):
    x = x - lr*dg(x)

print("\tGradient descent minimum: x =", x, ";\ty =", g(x))

#   (2) Newton method
#   For Newton (which solves dg(x)=0), also check the sign of d2g at the answer:
#   d2g > 0 means a minimum, d2g < 0 means a maximum.
x0 = 2
newtonMin = newton(dg, x0, fprime=d2g)

sign = d2g(newtonMin)
print("\tNewton's method", ("minimum" if sign > 0 else "maximum" if sign < 0 else "flat point") + ": x =", newtonMin, ";\ty =", g(newtonMin))

#   (3) SLSQP Method
x0 = 2
slsqpMin = minimize(g, x0, method="SLSQP")

print("\tSLSQP minimum: x =", slsqpMin.x[0], ";\ty =", g(slsqpMin.x[0]))


#   In your README note: do the methods agree? did Newton find a minimum or
#   another stationary point? how did the starting point change the result?
