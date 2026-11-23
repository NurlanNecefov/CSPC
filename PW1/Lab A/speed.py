import numpy as np
import pytest
import time
from decay import simulate, simulate_loop

def running_time_of_simulate_loop():
    startLoop = time.perf_counter()
    simulateLoop = simulate_loop(1000, 0.4)
    endLoop = time.perf_counter()

    startNumpy = time.perf_counter()
    simulateNumpy = simulate(1000, 0.4)
    endNumpy = time.perf_counter()

    speedLoop = endLoop-startLoop
    speedNumpy = endNumpy - startNumpy

    speedup = speedLoop/speedNumpy

    print(f"Speed of pure-Python function: {speedLoop} sec\nSpeed of the function written with Numpy: {speedNumpy} sec")
    print(f"\nNumpy version is {speedup:.0f}x faster than pure-Python version.")

running_time_of_simulate_loop()
