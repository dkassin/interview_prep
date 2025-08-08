def surrounding_region(board):
    if not board or not board[0]: return []

    rows, cols = len(board), len(board[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    def dfs_helper(r,c):
        if r < 0 or r>= rows or c < 0 or c>= cols:
            return
        if board[r][c] != "O":
            return
        board[r][c] = "T"
        for dr,dc in directions:
            dfs_helper(r+dr,c+dc)
    
    for r in range(rows):
        if board[r][0] == "O":
            dfs_helper(r,0)
        if board[r][cols-1] == "O":
            dfs_helper(r,cols-1)
    for c in range(cols):
        if board[0][c] == "O":
            dfs_helper(0,c)
        if board[rows-1][c] == "O":
            dfs_helper(rows-1,c)
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "T":
                board[r][c] = "O"
