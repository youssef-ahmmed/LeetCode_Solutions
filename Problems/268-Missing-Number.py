class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_sum = sum(nums)
        total_sum = sum([n for n in range(len(nums) + 1)])

        return total_sum - nums_sum
