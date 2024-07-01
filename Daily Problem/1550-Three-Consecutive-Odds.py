class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        def is_odd(nums):
            return nums[0] % 2 == 1 and nums[1] % 2 == 1 and nums[2] % 2 == 1

        for i in range(len(arr) - 2):
            if is_odd(arr[i:i + 3]):
                return True

        return False
    