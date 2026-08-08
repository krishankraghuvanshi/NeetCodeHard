class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        S = len(s)
        T = len(t)
        
        dp = {}
        def f(i, j):
            if i == S and j != T:
                return 0
            if j == T:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]    
            if s[i] == t[j]:
                dp[(i, j)] = f(i+1, j+1) + f(i+1, j)
                return dp[(i, j)]
            dp[(i, j)] = f(i+1, j)  
            return dp[(i, j)] 
        return f(0, 0)        
