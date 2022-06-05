import numpy as np


# 직접
def getMinorMatrix(A, i, j):
    n = len(A)
    M = np.zeros((n - 1, n - 1))
    for a in range(0, n - 1):
        k = a if (a < i) else a + 1
        for b in range(0, n - 1):
            l = b if (b < j) else b + 1
            M[a, b] = A[k, l]
    return M


# numpy module 사용
def getMinorMatrix2(A, i, j):
    a = np.delete(A, i, axis=0)
    a = np.delete(a, j, axis=1)
    return a


# 2*2 행렬의 행렬식
def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


A = np.array([[1, 2, 3],
              [3, 2, 1],
              [4, 4, 5]])

# 첫번째 행을 기준으로 determinant를 계산 해보겠습니다.
A[0][0] * det(getMinorMatrix2(A, 0, 0)) - A[0][1] * det(getMinorMatrix2(A, 0, 1)) + A[0][2] * det(getMinorMatrix2(A, 0, 2))