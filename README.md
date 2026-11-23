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
![Decay plot](https://github.com/NurlanNecefov/images_for_readme/blob/main/pw1_figure.png?raw=true)

**Conclusion:**
- In this lab we learned how to draw a graph of given data and automating this with using snakemake.

---
## PW2 - Lab A: Motion from Tracking Data


**What I Built:**
- We have y position and time datas of a freefall object. These datas have some noises. This program cleans these noises, calculates the velocity and acceleration, finds the mean acceleration, standard deviation of acceleration, and largest difference between original and recovered positions. As a bonus, it calculates same things on 2d plane trajectory. We used $v = \sqrt{v_x^2 + v_y^2}$ formula to calculate magnitude of velocity.

**How to Use?:**
- run `python "CSPC/PW2/Lab A/analysis_STUDENT.py` then it will creates *motion.png* and *motion_trajectory.png* at the location of plot.py

**Expected Outputs:**
- motion:
![motion.png](https://github.com/NurlanNecefov/images_for_readme/blob/main/pw2_lab_a_motion.png?raw=true)
- motion_trajectory:
![motion_trajectory.png](https://github.com/NurlanNecefov/images_for_readme/blob/main/pw2_lab_a_motion_trajectory.png?raw=true)

**Questions:**
- ***Part 3: The mean acceleration is near −9.81, but print its
standard deviation too (a.std()). Notice it is large: the individual acceleration values swing
wildly even though the position data looked smooth.***

    Because of the inaccuracy of measurements, there is some *little* noises. When we get the gradient of them, these noises gradually increases. After 2 derivations we get acceleration but its noises much bigger than our measurements. Acceleration has biggest noise both because it's 2 derivatives of position so its noises increased and we can't filter them using derivative and integral method.

---
## PW2 - Lab B: Optimization in Chemistry


**What I Built:**
- Computers can't calculate derivative like a person, instead we use some mathematical methods to calculate derivative and some of them have small errors. In this lab we used these methods for optimizing chemical calculations.
We used:

    - Gradient Descent
    - Newton's Method
    - SLSQP Method
    
    and compared their results.

**Questions:**
1. do the methods agree? did Newton land on a minimum or another stationary point? how did the starting point change the result? *(Part 2B)*
    
    Gradient descent and SLSQP methods gives nearly the same results every time. On the other hand, Newton's method finds local minimum or maximum depends on starting point.

**How to Use?:**
- run this command in `CSPC` folder

      cd "PW2/Lab B" && python -c "print('\n\nwarmup_STUDENT.py\n')" && python warmup_STUDENT.py && python -c "print('\n\nkinetics_STUDENT.py\n')" && python kinetics_STUDENT.py && python -c "print('\n\ntitration_STUDENT.py\n')" && python titration_STUDENT.py && python -c "print('\n\nequilibrium_STUDENT.py\n')" && python equilibrium_STUDENT.py
- just for image outputs, run `cd "PW2/Lab B" && snakemake --cores 3` in CSPC folder

**Expected Outputs:**
1. warmup_STUDENT.py:

        For f(x) = (x-3)**2 + 1:
            x0 = 0

            Gradient descent minimum: x = 2.9999999993888893 ;      y = 1.0
            Newton's method minimum: x = 3.0 ;      y = 1.0
            SLSQP minimum: x = 3.0 ;        y = 1.0

        For g(x) = x**4 - 3*x**2 + x + 5
            x0 = 0:

            Gradient descent minimum: x = -1.3008395659415772 ;     y = 1.48609496106521
            Newton's method maximum: x = 0.16993844331159128 ;      y = 5.084135220710943
            SLSQP minimum: x = -1.3008569447162184 ;        y = 1.4860949632256304


            x0 = 2:

            Gradient descent minimum: x = -1.3008395659415772 ;     y = 1.48609496106521
            Newton's method minimum: x = 1.1309011226299859 ;       y = 3.929769818223846
            SLSQP minimum: x = -1.3006394477423422 ;        y = 1.4860952474858662

2. kinetics_STUDENT.py:

        Fitted k: 0.2617613705507395
    <img src="https://github.com/NurlanNecefov/images_for_readme/blob/main/pw2_lab_b_kinetics.png?raw=true">

3. titration_STUDENT.py:

        Equivalence point: 50.0 mL
    <img src="https://github.com/NurlanNecefov/images_for_readme/blob/main/pw2_lab_b_titration.png?raw=true">

4. equilibrium_STUDENT.py:

        Reaction Extent (x):
        Newton:          0.6638476669609827
        SLSQP:           0.6638474284044567
        Difference:      2.38556526088729e-07

        Equilibrium amounts:
        H2: 0.33615233303901726
        I2: 0.33615233303901726
        HI: 1.3276953339219655
    <img src="https://github.com/NurlanNecefov/images_for_readme/blob/main/pw2_lab_b_equilibrium.png?raw=true">
