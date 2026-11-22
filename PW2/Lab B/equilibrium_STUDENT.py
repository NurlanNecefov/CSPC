"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.
def k_imbalance(x): return (2*x)**2/((a-x)*(b-x)) - K
def dk_imbalance(x): return 4*x*(2*a*b - (a+b)*x) / ((a-x)**2 * (b-x)**2)

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.
x0 = 0.5
newton_root = newton(k_imbalance, x0, fprime=dk_imbalance)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.
x0 = [0.5]
def square_k_imbalance(x): return k_imbalance(x[0])**2

minimized_k_imbalance = minimize(
    square_k_imbalance,
    x0=x0,
    method="SLSQP",
    bounds=[(0, 0.999)]
)

slsqp_root = minimized_k_imbalance.x[0]

difference = newton_root - slsqp_root

print("Reaction Extent (x):")
print("Newton:\t\t", newton_root)
print("SLSQP:\t\t", slsqp_root)
print("Difference:\t", difference)

# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.
H2_eq = a - newton_root
I2_eq = b - newton_root
HI_eq = 2 * newton_root

print("\nEquilibrium amounts:")
print("H2:", H2_eq)
print("I2:", I2_eq)
print("HI:", HI_eq)

x_values = np.linspace(0, 0.999, 200)

H2 = a - x_values
I2 = b - x_values
HI = 2 * x_values

fig, ax = plt.subplots(1, 1, figsize=(10, 5))

ax.plot(x_values, H2, label="H2")
ax.plot(x_values, I2, label="I2")
ax.plot(x_values, HI, label="HI")

# Mark equilibrium
ax.axvline(newton_root, color="red", linestyle="--", label="Equilibrium")

ax.set_xlabel("Extent (x)")
ax.set_ylabel("Amount (mol)")
ax.set_title("Chemical Equilibrium")
ax.legend()
ax.grid(True)

plt.savefig("equilibrium.png")