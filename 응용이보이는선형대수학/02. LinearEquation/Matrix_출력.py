def matrix_print(name, A):
    print("---", name, "---")
    (n, m) = A.shape
    for i in range(0, n):
        line = ""
        for j in range(0, m):
            line += "{0:.2f}".format(A[i, j]) + "\t"
            if j == m - 2:
                line += "ㅣ"
        print(line)
    print("")
