import numpy as np

# 3*3 행렬 생성
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])


# 3*1 벡터 생성
V = np.array([[1],
              [2],
              [3]])

# 형태 보기
A.shape

# 행렬 벡터 연산
print(A+V)
print(A-V)
print(A*V)