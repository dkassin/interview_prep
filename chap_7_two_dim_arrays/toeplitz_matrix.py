def toeplitz_matrix(matrix) -> bool:
    rows = len(matrix)
    column = len(matrix[0])
    for i in range(rows-1):
        for j in range(column-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
        return True

matrix_1 = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
assert toeplitz_matrix(matrix_1) == True

matrix_2 = [[1,2],[2,2]]
assert toeplitz_matrix(matrix_2) == False