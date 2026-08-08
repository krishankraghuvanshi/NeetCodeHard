class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        maxq = deque()
        ans = []

        left = 0
        right = 0

        while right < len(nums):
            while len(maxq) and maxq[-1][1] < nums[right]:
                maxq.pop()
            maxq.append((right, nums[right]))    
            if right - left + 1 > k:   
                if maxq[0][0] == left:
                    maxq.popleft()
                left += 1
            if right - left + 1 == k:   
                # print(maxq)     
                ans.append(maxq[0][1])
            # print(right, left, maxq)    
            right += 1
        return ans                 