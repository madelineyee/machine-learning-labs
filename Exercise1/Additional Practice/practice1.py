import numpy as np

def my_gd (year, price):
    t0 = t1 = 0
    n = len(x)
    iterations = 100
    a = 0.1

    for i in range(n):
        h = t0 +t1*x
        cost = (1/(2*n))*sum(val**2 for val in [h-y])
        t0 = t0 - a*np.diff(cost,t0)