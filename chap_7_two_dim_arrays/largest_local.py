def largest_local(grid):
    rows, cols = len(grid), len(grid[0])
    result = []
    for i in range(rows-2):
        row_result = []
        for j in range(cols-2):
            max_val = float('-inf')
            for r in range(i, i+3):
                for c in range(j, j+3):
                    max_val = max(max_val,grid[r][c])
            row_result.append(max_val)
        result.append(row_result)
    return result


assert largest_local([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]) == [[9,9],[8,6]]