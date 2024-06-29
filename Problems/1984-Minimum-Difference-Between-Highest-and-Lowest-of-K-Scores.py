class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mn_diff = nums[k - 1] - nums[0]

        for i in range(1, len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            mn_diff = min(mn_diff, diff)

        return mn_diff
