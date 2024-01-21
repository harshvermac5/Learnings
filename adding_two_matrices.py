def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Dimensions of Matrices must be matched!"
    
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)    
        
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

sum_of_matrices = add_matrices(matrix1, matrix2)

print(sum_of_matrices)

'''Here's what each part does:

for i in range(len(mat1)):

This outer loop iterates over the rows of mat1. The variable i takes on values from 0 to len(mat1) - 1.
row = []

Inside the outer loop, a new list named row is created. This list will represent a row in the result matrix.
for j in range(len(mat1[0])):

This inner loop iterates over the columns of the matrices mat1 and mat2. The variable j takes on values from 0 to len(mat1[0]) - 1.
row.append(mat1[i][j] + mat2[i][j])

Within the inner loop, elements at the same position (i, j) from mat1 and mat2 are added together, and the result is appended to the row list.
result.append(row)

After the inner loop completes for a particular row (i), the entire row is appended to the result list. This process is repeated for each row in the matrices.
return result

Finally, the function returns the result list, which represents the sum of the input matrices.'''