def flood_fill(image, sr:int, sc: int, color:int):
    visited = set()
    check_value = image[sr][sc]
    def dfs(i,j):
        if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):
                return
        
        if (i,j) in visited:
                return
        
        if image[i][j] == check_value:
                image[i][j] = color
        else:
            return
        
        visited.add((i,j))
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                dfs(ni,nj)
    
    dfs(sr,sc)
    return image