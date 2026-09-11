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