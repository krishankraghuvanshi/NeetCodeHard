class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:


        @cache


        def f(index, left):
            if index == len(nums):
                if left == 0:
                    return 0
                return float("inf")   
            if left == 0:
                return float("inf")     


            res = float("inf")

            cur = 0
            for i in range(index, len(nums)):
                cur += nums[i]
                res = min(res, max(cur, f(i+1, left-1)))
                if cur > res:
                    break
            return res 
        return f(0, k)           


        
