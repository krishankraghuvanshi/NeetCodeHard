class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        left_best = 0
        right_best = 0
        ans = 0
        while left <= right:
            left_best = max(left_best, height[left])
            right_best = max(right_best, height[right])
            if left_best < right_best:
                ans += (left_best-height[left])
                left += 1
            else:
                ans += (right_best-height[right])
                right -= 1
        return ans            

        
