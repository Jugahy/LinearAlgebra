import numpy as np
import Matrix_출력


# 가우스-조단 소거법 함수
def Gauss(A):
    (n, m) = A.shape

    # i번째 열레서 절댓값이 최대인 성분의 행 선택
    for i in range(0, n):
        maxEl = abs(A[i, i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k, i]) > maxEl:
                maxEl = abs(A[k, i])
                maxRow = k

        # 현재 i번째 행과 최댓값을 갖는 행 maxRow의 교환
        for k in range(i, m):
            tmp = A[maxRow, k]
            A[maxRow, k] = A[i, k]
            A[i, k] = tmp

        # 추축성분을 1로 만들기
        piv = A[i, i]
        for k in range(i, m):
            A[i, k] = A[i, k] / piv

        # 현재 i번째 열의 i번째 행을 제외한 모든 성분을 0으로 만들기
        for k in range(0, n):
            if k != i:
                c = A[k, i] / A[i, i]
                for j in range(i, m):
                    if i == j:
                        A[k, j] = 0
                    else:
                        A[k, j] = A[k, j] - c * A[i, j]

        # 진행 과정 출력
        Matrix_출력.matrix_print(str(i + 1) + "번째 반복", A)

    # Ax=b의 해 반환
    x = np.zeros(n)
    for i in range(0, n):
        x[i] = A[i, n]
    return x

# 숫자 뒤에 점은 ".0"을 표현 한거임
# 구하고 싶은 연립선형방정식의 첨가행렬
A = np.array([[2., 2., 4., 18.], [1., 3., 2., 13.], [3., 1., 3., 14]])

Matrix_출력.matrix_print("문제", A)   # 첨가행렬 출력
x = Gauss(A)    # 가우스 조간 소거법 적용

# 출력
(n, m) = A.shape
line = "해:\t"
for i in range(0, n):
    line += "{0:.2f}".format(x[i]) + "\t"
print(line)
