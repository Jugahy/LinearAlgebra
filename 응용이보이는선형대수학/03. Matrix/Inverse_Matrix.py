import numpy as np

A = np.array([[2, 4],
              [1, -3]])


# 2*2 행렬의 역행렬!
def inverse(A):
    # 행렬식 구하기
    determinant = A[0][0] * A[1][1] - A[0][1] * A[1][0]

    # 행렬 바꾸기
    tmp = A[0][0]
    A[0][0] = A[1][1]
    A[1][1] = tmp
    A[0][1] = -A[0][1]
    A[1][0] = -A[1][0]

    return 1 / determinant * A


# numpy 모듈 사용하여 역행렬 구하기
np.linalg.inv(A)
