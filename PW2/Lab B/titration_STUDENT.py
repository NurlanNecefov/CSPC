"""
PW2 Lab B Part 5 (bonus) -- find a titration's equivalence point.

titration.csv holds a titration curve: pH versus the volume of base added.
The equivalence point is the volume where the pH changes fastest (the steep
jump). Numerically, that is where the SLOPE of the pH curve is largest.
Run:  python titration.py
"""
import numpy as np
import matplotlib.pyplot as plt

# TODO 1: read titration.csv (columns volume_base, pH) into arrays V, pH.
data = np.loadtxt(fname="titration.csv", delimiter=',', skiprows=1)
V = data[:, 0]
pH = data[:, 1]

# TODO 2: compute the slope of the pH curve with np.gradient(pH, V), and find
#         the volume where that slope is largest (np.argmax). That is the
#         equivalence point. Print it.
slope_pH = np.gradient(pH, V)
equivalence_point = V[np.argmax(slope_pH)]
print("Equivalence point:", equivalence_point, "mL")

# TODO 3: make two plots side by side: (left) pH vs volume with a line at the
#         equivalence point; (right) the slope vs volume, showing it peaks
#         at the equivalence point. Save as titration.png.
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

ax[0].plot(V, pH)
ax[0].set_xlabel("Volume (mL)")
ax[0].set_ylabel("pH")
ax[0].axvline(x=equivalence_point, color="red", label="Equivalence point", linestyle="-")
ax[0].legend()
ax[0].grid(True)

ax[1].plot(V, slope_pH)
ax[1].set_xlabel("Volume (mL)")
ax[1].set_ylabel("Slope")
ax[1].axvline(x=equivalence_point, color="red", label="Equivalence point", linestyle="-")
ax[1].legend()
ax[1].grid(True)

plt.savefig("titration.png", dpi=500)