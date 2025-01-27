class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        st = 0
        count = 0
        for en in range(2, len(nums)):
            if nums[en] - nums[en - 1] == nums[en - 1] - nums[en - 2]:
                count += (en - st - 1)
            else:
                st = en - 1

        return count
