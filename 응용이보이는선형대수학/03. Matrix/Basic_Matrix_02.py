import numpy as np

A = np.array([[1., 2.],
              [3., 4.]])

B = np.array([[2., 2.],
              [1., 3.]])

# 행렬의 곱 AB
np.matmul(A, B)

# 행렬의 거듭제곱
np.linalg.matrix_power(A, 2)

# 전치
A.T

# 대각행렬 diag(1,2,3) 생성
np.diag([1, 2, 3])

# 블록행렬 생성
D11 = np.array([[1,2],[3,4]])
D12 = np.array([[5],[6]])
D21 = np.array([[7, 7]])
D22 = np.array([[8]])

D = np.block([[D11, D12], [D21, D22]])