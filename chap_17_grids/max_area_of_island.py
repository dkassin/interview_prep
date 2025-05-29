def max_area_of_island(grid)-> int:
    visited = set()
    def dfs(i,j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        
        if (i,j) in visited or grid[i][j] == 0:
            return 0
        
        visited.add((i,j))
        island = 1
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            islands += dfs(ni,nj)
        return islands
    
    max_val = 0
    for i in range(len(grid)):
            for j in range(len(grid[0])):
                 if grid[i][j]== 1 and (i,j) not in visited:
                      max_val = max(max_val, dfs(i,j))

    return max_val