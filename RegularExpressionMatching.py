class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        S, P = len(s), len(p)
        dp = [[-1] * (P+1) for _ in range(S+1)]
        def solve(i, j):
            if j == P:
                return i == S  
            if dp[i][j] != -1:
                return dp[i][j]    
            res = False
            if j + 1 < P and p[j+1] == '*':
                res = res or ((i < S and (s[i] == p[j] or p[j] == '.')) and solve(i + 1, j)) or solve(i, j + 2)
            else:
                res = res or (i < S and (s[i] == p[j] or p[j] == '.')) and solve(i + 1, j + 1)
            dp[i][j] = res    
            return res
        return solve(0, 0)            
