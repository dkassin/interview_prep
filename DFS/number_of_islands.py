def number_of_islands(grid):
    if not grid:return 0
    count = 0
    visited = set()
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    def dfs_helper(r,c):
        if r < 0 or r >= len(grid) or c < 0 or c>= len(grid[0]):
                return
        if (r,c) in visited or grid[r][c] == 0:
                return
        visited.add((r,c))
        for dr,dc in directions:
              dfs_helper(r + dr, c + dc)
    
    for r in range(len(grid)):
          for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                      dfs_helper(r,c)
                      count += 1
    return count

## You can avoid using visited by marking visited cells with 0 so they would be skipped
