class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0]*n for _ in range(n)]
        count = [0]
        def is_valid(row, col):
            for r in range(row-1, -1, -1):
                if board[r][col] == 1:
                    return False
            for c in range(col-1, -1, -1):
                if board[row][c] == 1:
                    return False
            r, c = row-1, col-1
            while r >= 0 and c >= 0:
                if board[r][c] == 1:
                    return False
                r -= 1
                c -= 1  
            r, c = row-1, col+1    
            while  r >= 0 and c < n:
                if board[r][c] == 1:
                    return False
                r -= 1
                c += 1
            return True              
        def back(row):
            if row == n:
                print(board)
                count[0] += 1
                return 
            for col in range(n):
                board[row][col] = 1
                if is_valid(row, col):
                    back(row+1)
                board[row][col] = 0
        back(0)  
        return count[0]
