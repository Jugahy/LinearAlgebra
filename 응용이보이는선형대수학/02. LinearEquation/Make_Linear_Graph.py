import matplotlib.pyplot as plt
import numpy as np

# x 범위(linspace : -10~11 사이 값 중에서 20개 뽑아)
x = np.linspace(-10,11,20)

# x축과 y축에 label 이름
plt.xlabel("x axis")
plt.ylabel("y axis")

# 그래프의 배경 색, 간격, 줄 스타일
plt.grid(color="gray", alpha=.5, linestyle="--")

# 함수
y1 = 3 * x + 6
y2 = 3 * x + 3

# x의 범위와 y1의 함수를 사용하여 그래프 그림
# y1함수에 x값 하나씩 대입해서 그래프 그림
plt.plot(x, y1, label="y1")
plt.plot(x, y2, label="y2")

# 범례 작성
plt.legend()

# 그래프 보기
plt.show()
