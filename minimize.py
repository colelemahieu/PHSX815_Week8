# HW 9 (minimize)

# import packages
import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *
from scipy import optimize

# define function
def func(x):
    return (x-5)**2 + 2

# use Brent's method from scipy
result = optimize.minimize_scalar(func)
min = result.x
print("The minimum is at (%.3f, %.3f)" %(min,func(min)))
