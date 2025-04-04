def construct_2d_array(original, m, n):
    matrix = [[0] *n for _ in range(m)]
    matrix_rows = len(matrix)
    matrix_col = len(matrix[0])
    for i in range(matrix_rows):
        for j in range(matrix_col):
            if len(original) == 0:
                return []
            value = original.pop(0)
            matrix[i][j] = value
    
    if len(original) != 0:
        return []
    else:
        return matrix
    

def construct_2d_array_2(original, m, n):
    matrix = [[0]*n for _ in range(m)]
    location = 0
    for i in range(m):
        for j in range(n):
            if location >= len(original):
                return []
            matrix[i][j] = original[location]
            location += 1

    if location < len(original):
        return []
    else:
        return matrix
    

assert construct_2d_array_2([1,2,3,4],2,2) == [[1,2],[3,4]]
assert construct_2d_array_2([1,2,3],1,3) == [[1,2,3]]
assert construct_2d_array_2([1,2],1,1) == []

## Can we go over how you would get to the optimal solutions from the problem
## The solution that i came up with seems like the most intuitive to me