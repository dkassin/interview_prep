def exist(board, word: str) -> bool:
    visited = set()
    word = [i for i in word]
    def dfs(i,j, index):
        if len(word) == index:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return 
        
        if (i,j) in visited:
            return False
        
        if board[i][j] != word[index]:
            return False

        visited.add((i,j))
        index += 1
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if dfs(ni,nj, index):
                return True
        visited.remove((i, j))
        return False
            
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i,j,0):
                return True
    return False
