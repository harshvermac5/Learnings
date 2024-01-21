def multiply_matrices(mat1, mat2):

    #assigning values
    row1, col1, row2, col2 = len(mat1), len(mat1[0]), len(mat2), len(mat2[0])

    if col1 != row2:
        return "Matrix multiplication not possible"
    
    #initialising a empty matrix with 0
    result = [[0 for _ in range(col2)]for _ in range(row1)]

    for i in range(row1):
        for j in range(col2):
            for k in range(col1):
                result [i][j] += mat1[i][j] * mat2[k][j]

    return result

#for example:

matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

multiple_of_matrices = multiply_matrices(matrix1, matrix2)

print(multiple_of_matrices)