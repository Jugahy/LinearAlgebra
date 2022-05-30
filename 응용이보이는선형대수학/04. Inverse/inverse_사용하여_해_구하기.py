"""
Solutions of systems of linear equations
    2x1 - x2 + x3 = -2
    x1 + 3x2 - x3 = 10
    x1 +     + 2x3 = -8
"""

import numpy as np

A = np.array([[2, -1, 1],
              [1, 3, -1],
              [1, 0, 2]])

b = np.array([[-2],
              [10],
              [-8]])

inverse_A = np.linalg.inv(A)

x = np.matmul(inverse_A, b)

print(x)
