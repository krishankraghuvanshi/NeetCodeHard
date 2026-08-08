class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        #cycle sort

        index1 = 0

        while index1 < len(nums):
            index2 = nums[index1]-1
            if 0 < nums[index1] <= len(nums) and nums[index1] != nums[index2]:
                nums[index1], nums[index2] = nums[index2], nums[index1]
            else:
                index1 += 1
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1       

