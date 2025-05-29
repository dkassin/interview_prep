def is_valid_sudoku(board) -> bool:
    transposed_board = [[row[i] for row in board] for i in range(len(board[0]))]
    for row in board:
        if not valid_row(row):
            return False
    
    for column in transposed_board:
        if not valid_row(column):
            return False
    
    check_hash = {}
    for row in range(len(board)):
        for column in range(len(board[0])):
            square = ((row // 3), (column // 3))
            if square in check_hash:
                if board[row][column].isnumeric() and board[row][column] in check_hash[square]:
                    return False
                check_hash[square].append((board[row][column]))
            else:
                check_hash = []
                check_hash[square].append((board[row][column]))
    
    for key in check_hash:
        if not valid_row(check_hash[key]):
            return False
        
def valid_row(row):
    counter = 0
    for i in range(9):
        if row[i].isnumeric():
            counter += 1
    row_val = set(row)
    row_val.discard('.')
    return len(row_val) == counter



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
 
        n = len(board)
 
        for row in board:
            if not self.valid_row(row):
                return False
 
        for col in range(n):
            if not self.valid_row([board[i][col] for i in range(n)]):
                return False
 
        for row in range(0, n, 3):
            for col in range(0, n, 3):
                square = [
                    board[i][j]
                    for i in range(row, row + 3)
                    for j in range(col, col + 3)
                ]
                if not self.valid_row(square):
                    return False
 
        return True
 
    def valid_row(self, row):
        digits = [n for n in row if n != "."]
        return len(set(digits)) == len(digits)