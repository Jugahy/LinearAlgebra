import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])

# v1, v2, v3 벡터를 각각 행으로 하는 행렬 생성
A = np.vstack([v1, v2, v3])

# v1, v2, v3 벡터를 각각 열로 하는 행렬 생성
B = np.column_stack([v1, v2, v3])

# 행렬 C에 v3를 열로 추가하여 행렬 생성
C = np.array([[1, 2], [3, 4], [5, 6]])
D = np.column_stack([C, v3])

# 행렬 성분 접근
E = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

E[0, 3]

# 0~2 인덱스 전까지 2번째 성분
E[0:2, 2]

# 0~2 인덱스 전까지 2~4 전까지 성분
E[0:2, 2:4]

# 성분 변환
E[0, 0] = 100


