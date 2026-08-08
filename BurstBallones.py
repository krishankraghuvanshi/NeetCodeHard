class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)

        nums = [1] + nums + [1]
        @cache
        def solve(left, right):
            if left > right:
                return 0    
            best = 0
            for index in range(left, right + 1):
                best = max(best, nums[left-1] * nums[index] * nums[right + 1] + solve(left, index - 1) + solve(index + 1, right))
            return best

        return solve(1, N)        
