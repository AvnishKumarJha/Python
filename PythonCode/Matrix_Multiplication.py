matrix1 = [[2, 3, 4],
        [5, 6, 7]]

matrix2 = [[8, 9],
        [10, 11],
        [12, 13]]

result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for row in result:
    print(row)
