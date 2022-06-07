import numpy as np


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def det2(A):
    np.linalg.det(A)
