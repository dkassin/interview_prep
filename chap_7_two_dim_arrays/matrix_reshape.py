def matrix_reshape(matrix, r, c):
    result = [[0]*c for _ in range(r)]
    flattened_array = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            flattened_array.append(matrix[i][j])

    
    if len(flattened_array) != r*c:
        return matrix
    
    location = 0
    for i in range(r):
        for j in range(c):
            result[i][j] = flattened_array[location]
            location += 1
    
    return result

assert matrix_reshape([[1,2],[3,4]],1,4) == [[1,2,3,4]]
assert matrix_reshape([[1,2],[3,4]],2,4) == [[1,2],[3,4]]