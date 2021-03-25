# Python Neyman Construction

# import packages
import sys
import numpy as np
import matplotlib.pyplot as plt
from math import *
from Random import Random

# instantiate Random class
random = Random()

# experiment parameters
Nmeas = 1
Nexp = 1000
mu_exp = 0
sigma = 2

# arrays in which to collect data for the 2D histogram
mu_true_arr = []
mu_best_arr = []

# Loop through different mu values and use Gaussian for best guess
for i in range(-100,100):
    mu_true = float(i)/10.0

    for j in range(0, Nexp):
        mu_best = 0

        for k in range(0, Nmeas):
            x = float(random.box_muller(mu_true,sigma))
            mu_best += x

            mu_true_arr.append(mu_true)
            mu_best_arr.append(mu_best)






# plotting code
plt.figure()
plt.hist2d(mu_true_arr, mu_best_arr, bins=(150,150))
plt.title("2D Histogram")
plt.xlabel("Mu true")
plt.ylabel("Mu Measured")

plt.show()
