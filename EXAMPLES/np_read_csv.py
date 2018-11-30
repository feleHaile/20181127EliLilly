#!/usr/bin/env python
import numpy as np

a = np.loadtxt(
    '/Users/jstrick/Desktop/py3lilly/DATA/columns_of_numbers.txt',
    usecols=[2, 3],
    skiprows=1,
)

print(a)
print(a.shape)
print(a.size)

