"""
PW2 Lab A -- Motion from tracking data.

Read noisy free-fall position measurements, then:
  - differentiate once  -> velocity
  - differentiate twice -> acceleration (should be ~ constant -g, but noisy!)
  - integrate the acceleration back up -> recover velocity and position

Complete the TODOs. Run:  python analysis.py
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# TODO 1: read freefall.csv into arrays t and y
#         (hint: np.loadtxt with a comma delimiter, skipping the header)
t = np.loadtxt(fname="freefall.csv", delimiter=',', skiprows=1)[:, 0]
y = np.loadtxt(fname="freefall.csv", delimiter=',', skiprows=1)[:, 1]


# TODO 2: compute velocity v = derivative of y w.r.t. t   (np.gradient)
#         and acceleration a = derivative of v w.r.t. t    (np.gradient again)
#         Print the mean acceleration. Is it close to -9.81? Is it noisy?
v = np.gradient(y, t)
a = np.gradient(v, t)
mean_acceleration = np.mean(a)
print("Mean acceleration:", mean_acceleration) # result is -8.57968750000008. I think it's far away from -9.81. it's very noisy
print("Standard deviation of acceleration:", np.std(a)) # output: 28.71612572170628


# TODO 3: integrate a back up to recover velocity and position
#         (hint: cumulative_trapezoid(a, t, initial=0) + v[0], then again)
integrated_velocity = cumulative_trapezoid(a, t, initial=0) + v[0]
integrated_position = cumulative_trapezoid(integrated_velocity, t, initial=0) + y[0]
difference_position = np.abs(integrated_position - y)
max_difference = np.max(difference_position)
print("Max difference between original and recovered position:", max_difference)


# TODO 4: make a figure with 3 stacked panels: position, velocity, acceleration
#         vs time. Mark the true -9.81 line on the acceleration panel.
#         Save it as motion.png
fig, ax = plt.subplots(1, 3, figsize=(20, 5))
fig.subplots_adjust(wspace=0.5)

ax[0].plot(t, y, label="Original position")
ax[0].plot(t, integrated_position, label="Recovery position", linestyle=":")
ax[0].set_title("Position w.r.t. time", fontsize = 15)
ax[0].set_xlabel("t (seconds)", fontsize = 15)
ax[0].set_ylabel("y (meters)", fontsize = 15)
ax[0].legend(loc="upper right")

ax[1].plot(t, v, label="Original velocity")
ax[1].plot(t, integrated_velocity, label="Recovery velocity")
ax[1].set_title("Velocity w.r.t. time", fontsize = 15)
ax[1].set_xlabel("t (seconds)", fontsize = 15)
ax[1].set_ylabel("v (m/s)", fontsize = 15)
ax[1].legend(loc="upper right")

ax[2].plot(t, a, label="Calculated acceleration")
ax[2].axhline(y=-9.81, label="g = -9.81 m/s²", color="red", linestyle="--")
ax[2].set_title("Acceleration w.r.t. time", fontsize = 15)
ax[2].set_xlabel("t (seconds)", fontsize = 15)
ax[2].set_ylabel("a (m/s²)", fontsize = 15)
ax[2].legend(loc="upper right")

for axis in ax:
    axis.grid(True)

# plt.show()
plt.savefig("motion.png", dpi=500)


# Bonus (if time permits) — A 2D tracked trajectory
# TODO: Read trajectory.csv, plot the path (x vs y), then compute and plot the speed
#       over time using np.gradient on each coordinate.

t2 = np.loadtxt(fname="trajectory.csv", delimiter=',', skiprows=1)[:, 0]
x2 = np.loadtxt(fname="trajectory.csv", delimiter=',', skiprows=1)[:, 1]
y2 = np.loadtxt(fname="trajectory.csv", delimiter=',', skiprows=1)[:, 2]

v_x = np.gradient(x2, t2)
v_y = np.gradient(y2, t2)
v2 = np.sqrt(v_x**2 + v_y**2)

a_x = np.gradient(v_x, t2)
a_y = np.gradient(v_y, t2)
a2 = np.sqrt(a_x**2 + a_y**2)
mean_a2 = np.mean(a2)

integrated_v_x = cumulative_trapezoid(a_x, t2, initial=0) + v_x[0]
integrated_v_y = cumulative_trapezoid(a_y, t2, initial=0) + v_y[0]
integrated_v2 = np.sqrt(integrated_v_x**2 + integrated_v_y**2)

integrated_x2 = cumulative_trapezoid(integrated_v_x, t2, initial=0) + x2[0]
integrated_y2 = cumulative_trapezoid(integrated_v_y, t2, initial=0) + y2[0]

fig2, ax2 = plt.subplots(1, 5, figsize=(35,5))
fig2.subplots_adjust(wspace=0.5)

ax2[0].plot(x2, y2, label="Original position")
ax2[0].plot(integrated_x2, integrated_y2, label="Recovery position", linestyle=":")
ax2[0].set_title("Trajectory", fontsize = 15)
ax2[0].set_xlabel("x (meters)", fontsize = 15)
ax2[0].set_ylabel("y (meters)", fontsize = 15)
ax2[0].legend(loc="upper right")

ax2[1].plot(t2, x2, label="Original x position")
ax2[1].plot(t2, integrated_x2, label="Recovery x position", linestyle=":")
ax2[1].set_title("x position w.r.t. time", fontsize = 15)
ax2[1].set_xlabel("t (seconds)", fontsize = 15)
ax2[1].set_ylabel("x (meters)", fontsize = 15)
ax2[1].legend(loc="upper right")

ax2[2].plot(t2, y2, label="Original y position")
ax2[2].plot(t2, integrated_y2, label="Recovery y position", linestyle=":")
ax2[2].set_title("y position w.r.t. time", fontsize = 15)
ax2[2].set_xlabel("t (seconds)", fontsize = 15)
ax2[2].set_ylabel("y (meters)", fontsize = 15)
ax2[2].legend(loc="upper right")

ax2[3].plot(t2, v2, label="Original velocity")
ax2[3].plot(t2, integrated_v2, label="Recovery velocity")
ax2[3].set_title("velocity w.r.t. time", fontsize = 15)
ax2[3].set_xlabel("t (seconds)", fontsize = 15)
ax2[3].set_ylabel("v (m/s)", fontsize = 15)
ax2[3].legend(loc="upper right")

ax2[4].plot(t2, a2, label="Acceleration")
ax2[4].axhline(y=mean_a2, label="Mean acceleration", color="red")
ax2[4].set_title("acceleration w.r.t. time", fontsize = 15)
ax2[4].set_xlabel("t (seconds)", fontsize = 15)
ax2[4].set_ylabel("a (m/s²)", fontsize = 15)
ax2[4].legend(loc="upper right")

for axis in ax2:
    axis.grid(True)

plt.savefig("motion_trajectory.png", dpi=500)