#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random as rand

# -*- calculate sample standard deviation -*- #

def calculate_sd(k):
    # if the standard deviation is small enough,
    if np.std(k) < 0.0005:  # that is, less than 0.0005, then,
        return True  # return true

    else:  # if the standard deviation is still greater than the stipulated value
        k.clear()  # empty the vector and try again

    return False  # by default, return false, in case it hasn't returned true in the above condition


# -*- estimate pi -*- #

def estimate_pi(Seed=None):
    rand.seed(Seed)

    total_points = 0
    points_inside = 0

    k = []  # vector where estimates for the kappa ratio will be stored

    # auxiliary variable to avoid entering another function to check conditions
    k_aux = False

    while not k_aux:  # while the function does not return true
        # generate a random point between (0,1)
        if rand.random() ** 2 + rand.random() ** 2 <= 1:  # if it is a point inside
            points_inside += 1  # increase the count of points inside the circumference

            if total_points >= 10**7:  # if the total number of points is 10 million or more
                k.append(points_inside / total_points)  # calculate the ratio and store it

                if len(k) == 5000:  # if the sample of estimates already has 5000 terms
                    # calculate the sample standard deviation, and the function's response is stored in the auxiliary variable
                    k_aux = calculate_sd(k)

        total_points += 1

    # return your estimate of pi, that is, 4 times the kappa
    return 4 * np.mean(k)


# -*- main -*- #
base = np.pi * 0.05 / 100  # the maximum allowed deviation

pi_estimate = estimate_pi()  # function call
print("The estimate for pi is", round(pi_estimate, 5))

error = 100 * abs(np.pi - pi_estimate) / np.pi

if error > 0.05:
    print("It was not possible to achieve precision, so the deviation was",
          round(error, 3), "%")
else:
    print("The precision was respected, and the deviation was", round(error, 3), "%")
