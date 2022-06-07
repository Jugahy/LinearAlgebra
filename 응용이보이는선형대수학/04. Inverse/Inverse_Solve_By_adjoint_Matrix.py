"""
수반행렬을 이용하여 역행렬 구하기
수반행렬 : n차 정방행렬 A에 대해서 여인수를 성분으로 갖는 행렬의 전치행렬 [C_ij^T]
    소행렬식 : 행렬 A에서 성분 a_ij가 있는 i행과 j열을 제거한 행렬의 행렬식을 A_ij로 표현
    여인수 : 행렬식 계산 시 사용되는 a_ij의 소행렬식 A_ij와 (-1)^ij의 곱
    정방행렬 : 정사각행렬
    전치행렬 : 행렬의 행과 열 변경
    C_ij : 여인수를 보통 C로 표현

A^-1 = 1/|A| * adjA
"""
import numpy as np


# (2,2) determinant
def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


# 수반행렬
def AdjointMatrix(A):
    import math

    (n, m) = A.shape

    B = np.zeros((3, 3))

    for i in range(n):
        for j in range(m):
            a = np.delete(A, i, axis=0)
            a = np.delete(a, j, axis=1)
            B[i][j] = math.pow(-1, i + j) * det(a)
    return B.T


# numpy module 사용 원하는 행, 열 삭제
def getMinorMatrix2(A, i, j):
    a = np.delete(A, i, axis=0)
    a = np.delete(a, j, axis=1)
    return a


# 첫번째 행을 기준으로 determinant를 계산
def one_row_determinant(A):
    return A[0][0] * det(getMinorMatrix2(A, 0, 0)) - A[0][1] * det(getMinorMatrix2(A, 0, 1)) + A[0][2] * det(
        getMinorMatrix2(A, 0, 2))


A = np.array([[1, 4, 3],
              [2, 3, 2],
              [4, 2, 5]])

det_A = one_row_determinant(A)
adj_A = AdjointMatrix(A)
inverse_A = 1 / det_A * adj_A

print(inverse_A)
