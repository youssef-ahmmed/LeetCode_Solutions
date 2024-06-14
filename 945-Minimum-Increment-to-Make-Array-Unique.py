class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                temp = nums[i - 1] - nums[i] + 1
                cnt += temp
                nums[i] += temp

        return cnt
