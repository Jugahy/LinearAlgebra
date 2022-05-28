"""
Linear combination은 n차원에 n개의 벡터가 존재할 때 이 n개의 벡터들이 서로 스칼라 배를
통해 만들지 못한다면 n개의 벡터로 n차원의 모든 좌표를 표현 가능하다.

-> 이 것을 2차원을 예시로 직접 코드를 작성해보겠습니다.
"""

import matplotlib.pyplot as plt
import numpy as np
import random


# 스칼라 배를 통해 서로를 만들 수 없는 두 벡터
v1 = np.array([1, 2])
v2 = np.array([1, 3])


# 임의의 스칼라 배
x1 = [random.uniform(-1, 1) for i in range(10000)]
x2 = [random.uniform(-1, 1) for i in range(10000)]


# 그래프 형태
plt.figure(figsize=(10, 10))
plt.xlim(-0.5, 0.5)
plt.ylim(-0.5, 0.5)
plt.grid(linestyle="--")


# 좌표평면에 벡터 표시
# plt.arrow(0, 0, v1[0], v1[1], head_width=.5, head_length=.5, color="red")


# 일차결합을 통해 새로운 벡터 만들고 점 찍어줌
for i, j in zip(x1, x2):
    v1 = [v1[k] * i for k in range(len(v1))]
    v2 = [v2[p] * j for p in range(len(v2))]
    vv = [v1[l] + v2[l] for l in range(len(v1))]
    plt.scatter(vv[0], vv[1])
    v1 = [1, 2]
    v2 = [1, 3]


plt.show()


