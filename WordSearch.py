class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        W = len(word)

        if R*C < W: return False

        visited = [[False] * C for _ in range(R)]

        def solve(i, j, index):
            if index >= W:
                return True

            if not (0 <= i < R and 0 <= j < C):
                return False

            if visited[i][j]:
                return False        

            if board[i][j] != word[index]:
                return False

            visited[i][j] = True

            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = i+di, j+dj

                if solve(ni, nj, index + 1):
                    return True

            visited[i][j] = False        
            return False   

        for i in range(R):
            for j in range(C):
                if solve(i, j, 0):
                    return True
        return False                     
