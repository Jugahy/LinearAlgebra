import numpy as np

A = np.array([[1, 2],
              [3, 4]])


# 구현
print(A[0][0] * A[1][1] - A[0][1] * A[1][0])

# numpy module 사용
print(np.linalg.det(A))