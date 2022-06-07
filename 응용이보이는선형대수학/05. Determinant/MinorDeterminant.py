import TwoDeterminant

def MinorDeterminant(A):
    import numpy as np

    (n, m) = A.shape

    B = np.zeros((3, 3))

    for i in range(n):
        for j in range(m):
            a = np.delete(A, i, axis=0)
            a = np.delete(a, j, axis=1)
            B[i][j] = TwoDeterminant.det(a)

    return B
