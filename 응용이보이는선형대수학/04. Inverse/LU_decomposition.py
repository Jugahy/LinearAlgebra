import numpy as np

A = np.array([[1, 2, 3],
              [1, 3, 5],
              [1, 5, 12]])

L = np.tril([[1, 2, 3],
             [1, 3, 5],
             [1, 5, 12]])

U = np.triu([[1, 2, 3],
             [1, 3, 5],
             [1, 5, 12]])

print(A)
print("---------------------")
print(L)
print("---------------------")
print(U)
print("---------------------")
print(np.matmul(L, U))
