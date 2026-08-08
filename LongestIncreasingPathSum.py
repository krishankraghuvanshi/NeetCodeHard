class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])

        dp = {}

        def dfs(i, j):
            if (i,j) in dp:
                return dp[(i, j)]

            res = 1

            for di, dj in [(1, 0), (0, -1), (0, 1), (-1, 0)]:
                ni, nj = i+di, j+dj
                if 0<=ni<r and 0<=nj<c and matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1+dfs(ni, nj))
                    
            dp[(i, j)] = res
            return dp[(i, j)]

        res = 0
        for i in range(r):
            for j in range(c):
                res = max(res, dfs(i, j))
        return res
