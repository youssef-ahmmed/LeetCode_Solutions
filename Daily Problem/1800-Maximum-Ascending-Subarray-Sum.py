class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = nums[0]
        max_sum = curr

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr += nums[i]
            else:
                curr = nums[i]
            max_sum = max(max_sum, curr)    
        return max_sum
