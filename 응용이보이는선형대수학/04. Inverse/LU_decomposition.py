import numpy as np


# LU 분해 함수 짜는 중
def LU(A):
    (n, m) = A.shape

    p = 0

    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        for j in range(m):
            if i > j:
                for k in range(j - 1):
                    p += L[i][k] * U[k][j]
                L[i][j] = (A[i][j] - p) / U[j][j]
                p = 0
            elif i <= j:
                for k in range(i - 1):
                    p += L[i][k] * U[k][j]
                U[i][j] = A[i][j] - p
                p = 0
    return L, U


A = np.array([[1, 2, 3],
              [1, 3, 5],
              [1, 5, 12]])
# 상삼각행렬
L = np.tril(A)

# 하삼각행렬
U = np.triu(A)
