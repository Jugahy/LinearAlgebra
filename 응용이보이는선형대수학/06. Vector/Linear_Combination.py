"""
Linear combination은 n차원에 n개의 벡터가 존재할 때 이 n개의 벡터들이 서로 스칼라 배를
통해 만들지 못한다면 n개의 벡터로 n차원의 모든 좌표를 표현 가능하다.

-> 이 것을 직접 코드로 증명해보겠습니다.
"""

import matplotlib.pyplot as plt
import numpy as np

# 스칼라 배를 통해 서로를 만들 수 없는 두 벡터
v1 = np.array([1, 2])
v2 = np.array([1, 3])

# 임의의 스칼라 배
x1 = np.random.randint(-10, 11, 100)
x2 = np.random.randint(-10, 11, 100)

# 그래프 형태
plt.figure(figsize=(10, 10))
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.grid(linestyle="--")

# 좌표평면에 벡터 표시
# plt.arrow(0, 0, v1[0], v1[1], head_width=.5, head_length=.5, color="red")


for i, j in zip(x1, x2):
    plt.scatter(i * v1[0], j * v1[1])

plt.show()






# mult = [a[i]*2 for i in range(len(a))]
# print(mult)