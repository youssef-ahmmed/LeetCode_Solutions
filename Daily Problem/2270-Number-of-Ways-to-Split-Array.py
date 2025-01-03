class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left = ways = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left += nums[i]
            right = total - left

            if left >= right:
                ways += 1
            
        return ways
