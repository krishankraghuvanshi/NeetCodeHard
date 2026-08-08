class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        N = len(nums)
        @cache
        def solve(index):
            if index >= N:
                return 0
            res = float("-inf")    
            sm = 0
            for i in range(3):
                if index + i < N:
                    
                    sm += nums[index+i]
                    res = max(res, sm - solve(index+i+1))
            return res    
        r = solve(0)
        solve.cache_clear()

        if r > 0:
            return "Alice"
        elif r < 0:
            return "Bob"
        else:    
            return "Tie"               

