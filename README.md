# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
> Open CSPC folder location in terminal, then write:
```
conda env create -f "PW1/Lab A/environment.yml"
conda activate cspc
```

---
## PW1 - Lab A: Reproducible Foundations

**What I built:**
- There are two versions of a function in decay.py that calculate the ***N<sub>0</sub>e<sup>−λt</sup>*** formula.
- One is written in **pure-Python** using loops, while the other uses the **Numpy** library.
- The **test_decay.py** file tests the accuracy of the function.
- The **speed.py** file measures the running time of each function and compares them.

**Speed comparison of my tests (loop vs NumPy):**
- loop : 0.036588 s
- numpy : 0.000244 s
- speed-up: 150 x faster
**Tests:** all passing? (**yes** / no)

**Conclusion:**
- In this lab, we learned how to write a test file, calculate the running time of a code, use Git for version control, document the enviroment and more.

**Testing on another machine:**
- My classmate downloaded the repo and created same environment from environment.yml on his machine. Then run pytest -v command and speed.py file. The results are:

    **1.** pytest -v passed all 3 tests

    **2.** The output of speed test is

        loop: 0.033275 s
        numpy: 0.000517 s
        speed-up: 64x faster

---
## PW1 - Lab B: Data, Plotting, and Automation


**What I Built:**
- In plot.py, I write a code for creating the graph of given data from decay_observed.csv

**How to Use?:**
- run `snakemake --cores 1 figure.png` and it will creates figure.png at the location of plot.py

**Expected Output:**
![Decay plot](https://private-user-images.githubusercontent.com/106445856/673291103-bbbd91f9-dc35-4815-a129-3c321e5cfcaf.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTQwNzU1ODcsIm5iZiI6MTc5NDA3NTI4NywicGF0aCI6Ii8xMDY0NDU4NTYvNjczMjkxMTAzLWJiYmQ5MWY5LWRjMzUtNDgxNS1hMTI5LTNjMzIxZTVjZmNhZi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMTA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTEwN1QxODE0NDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iZjAzNmI2ZWM2MDQxMGY2MmNjNzg5MWFhM2UyNDQzMmFkYmFlM2FkNjYyYjQyM2M5OWU3MTcwZDRmODlmZTAxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.-pi2F0eHoUArEQiv8Fx2jW1MJZNlIIeR-opCymVHtak)

**Conclusion:**
- In this lab we learned how to draw a graph of given data and automating this with using snakemake.

---
## PW2 - Lab A: Motion from Tracking Data


**What I Built:**
- We have y position and time datas of a freefall object. These datas have some noises. This program cleans these noises, calculates the velocity and acceleration, finds the mean acceleration, standard deviation of acceleration, and largest difference between original and recovered positions. As a bonus, it calculates same things on 2d plane trajectory. We used $v = \sqrt{v_x^2 + v_y^2}$ formula to calculate magnitude of velocity.

**How to Use?:**
- run `python "CSPC/PW2/Lab A/analysis_STUDENT.py` then it will creates *motion.png* and *motion_trajectory.png* at the location of plot.py

**Expected Outputs:**
![motion.png](https://private-user-images.githubusercontent.com/106445856/698612714-cbaf9af7-2113-4b26-89e5-9ade00bbde78.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTQwNzUxNTYsIm5iZiI6MTc5NDA3NDg1NiwicGF0aCI6Ii8xMDY0NDU4NTYvNjk4NjEyNzE0LWNiYWY5YWY3LTIxMTMtNGIyNi04OWU1LTlhZGUwMGJiZGU3OC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMTA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTEwN1QxODA3MzZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0zZTVkYjM1ODBlMmVkNDkzYmU2MTc5ZDE3YzI3NDEzNWQ1Y2RmODYyZDlkZDFiMjU2M2ZjNjBiNWJiOGY4NGEzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.8rQTxAOe1CN1_HNgXoViuqPVI-e63ba52LZaZhLJn9Q)
![motion_trajectory.png](https://private-user-images.githubusercontent.com/106445856/698612713-6162d125-9ae7-4100-9493-7d895a146109.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTQwNzUxNTYsIm5iZiI6MTc5NDA3NDg1NiwicGF0aCI6Ii8xMDY0NDU4NTYvNjk4NjEyNzEzLTYxNjJkMTI1LTlhZTctNDEwMC05NDkzLTdkODk1YTE0NjEwOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYxMTA3JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MTEwN1QxODA3MzZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iMTExMjgwZjA0MWVmZTk2ZDdlMDJiOTM5YjdmMWYzMjBlNmVhMWViNjNhYTU3MjU0NjlmZGNlMWZkYjI0Mjk3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZwbmcifQ.FcYdk6Zhw-hW2j3e7xNTYfgRMQqkIMxVgLk-LkO38og)

**Questions:**
- ***Part 3: The mean acceleration is near −9.81, but print its
standard deviation too (a.std()). Notice it is large: the individual acceleration values swing
wildly even though the position data looked smooth.***

    Because of the inaccuracy of measurements, there is some *little* noises. When we get the gradient of them, these noises gradually increases. After 2 derivations we get acceleration but its noises much bigger than our measurements. Acceleration has biggest noise both because it's 2 derivatives of position so its noises increased and we can't filter them using derivative and integral method.