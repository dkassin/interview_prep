def island_perimeter(grid) -> int:
    visited = set((i,j))
    def dfs(i,j):
        # logic here
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and (ni, nj) not in visited:
                visited.add((ni,nj))
                dfs(ni,nj)
    
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            ## Logic can go here
            visited.add((i,j))
            dfs(i,j)
    