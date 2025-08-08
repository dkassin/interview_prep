def flood_fill(image, sr,sc,color):
    visited = set()
    directions = [(-1,0),(1,0),(0,-1),((0,1))]
    filled_color = image[sr][sc]

    def dfs_helper(r,c):
        if r < 0 or r>= len(image) or c < 0 or c >= len(image[0]):
            return
        if (r,c) in visited:
            return
        if image[r][c] != filled_color:
            return
        image[r][c] = color
        visited.add((r,c))
        for dr, dc in directions:
            dfs_helper(r + dr, c + dc)
        return
    dfs_helper(sr,sc)
    return image

## improved to check in place for repeating
def flood_fill(image, sr,sc,color):
    directions = [(-1,0),(1,0),(0,-1),((0,1))]
    filled_color = image[sr][sc]
    if filled_color == color: return image

    def dfs_helper(r,c):
        if r < 0 or r>= len(image) or c < 0 or c >= len(image[0]):
            return
        if image[r][c] != filled_color:
            return
        image[r][c] = color
        for dr, dc in directions:
            dfs_helper(r + dr, c + dc)
        return
    dfs_helper(sr,sc)
    return image