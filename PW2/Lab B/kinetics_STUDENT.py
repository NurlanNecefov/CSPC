"""
PW2 Lab B Part 3 -- fit a reaction's rate constant to measured data.

A first-order reaction decays as  C(t) = C0 * exp(-k*t).  You have noisy
concentration-vs-time measurements; find the k that best matches them.
Complete the TODOs. Run:  python kinetics.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# TODO 1: read kinetics.csv (columns time, concentration) into arrays t, C.
#         Set C0 = the first concentration.
data = np.loadtxt(fname="kinetics.csv", delimiter=",", skiprows=1)
t = data[:, 0]
C = data[:, 1]
C0 = data[0, 1]

# TODO 2: write total_error(k) = sum of (measured - C0*exp(-k*t))^2.
#         This is the "how bad" number: small when the model matches the data.
def total_error(k): return np.sum((C - C0 * np.exp(-k[0] * t)) ** 2)

# TODO 3: minimise total_error with scipy.optimize.minimize (method "SLSQP",
#         bounds [(0, 5)], start x0=0.5). Print the fitted k.
x0 = 0.5
error_minimized = minimize(total_error, x0=x0, method="SLSQP", bounds=[(0, 5)])
k = error_minimized.x[0]

print("Fitted k:", k)

# TODO 4: plot the measured data (points) and your fitted curve (line) together.
#         Save as kinetics.png.
C_fitted = C0 * np.exp(-k * t)

fig, ax = plt.subplots(1, 1)

ax.plot(t, C, label="measured data", linestyle=":")
ax.plot(t, C_fitted, label="fitted curve")
ax.set_xlabel("time")
ax.set_ylabel("concentration")
ax.legend(loc="upper right")
ax.grid(True)

plt.savefig("kinetics.png", dpi=500)