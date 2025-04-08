class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if len(nums[i:]) == len(set(nums[i:])):
                return i // 3
            i += 3

        return i // 3
