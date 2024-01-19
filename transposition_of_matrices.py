def transpose_matrices(matrix):
    rows,cols = len(matrix), len(matrix[0])
    result = [[0 for _ in range(rows)]for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result

matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(transpose_matrices(matrix1))