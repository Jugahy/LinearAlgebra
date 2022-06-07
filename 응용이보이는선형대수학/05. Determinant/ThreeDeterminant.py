import numpy as np
import TwoDeterminant


# 직접 원하는 행, 열 삭제
def getMinorMatrix(A, i, j):
    n = len(A)
    M = np.zeros((n - 1, n - 1))
    for a in range(0, n - 1):
        k = a if (a < i) else a + 1
        for b in range(0, n - 1):
            l = b if (b < j) else b + 1
            M[a, b] = A[k, l]
    return M


# numpy module 사용 원하는 행, 열 삭제
def getMinorMatrix2(A, i, j):
    a = np.delete(A, i, axis=0)
    a = np.delete(a, j, axis=1)
    return a


# 첫번째 행을 기준으로 determinant를 계산
def one_row_determinant(A):
    A[0][0] * TwoDeterminant.det(getMinorMatrix2(A, 0, 0)) - A[0][1] * TwoDeterminant.det(getMinorMatrix2(A, 0, 1)) + A[0][2] * TwoDeterminant.det(getMinorMatrix2(A, 0, 2))
