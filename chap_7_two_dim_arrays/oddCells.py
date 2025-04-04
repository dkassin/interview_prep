def oddCells(m: int, n: int, indices):
    output = [[0]*n for _ in range(m)]
    for i in indices:
        for index, j in enumerate(i):
            if index == 0:
                for row_cell in range(n):
                    output[j][row_cell] += 1
            else:
                for column_cell in range(m):
                    output[column_cell][j] += 1
    
    count = 0
    for i in output:
        for j in i:
            if j % 2 != 0:
                count += 1
    return count 


assert oddCells(2,3,[[0,1],[1,1]]) == 6