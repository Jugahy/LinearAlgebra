"""
임의의 정방행렬 A에 대해 A+A transpose는 대칭행렬이고
A-A transpose는 반대칭행렬이다.
정방행렬 A는 대칭행렬과 반대칭행렬로 쪼갤 수 있습니다.

-> A = 1/2(A+A transpose) + 1/2(A-A transpose)를 증명해보겠습니다.
"""
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

trans_A = np.transpose(A)

print(1 / 2 * (A + trans_A) + 1 / 2 * (A - trans_A))
