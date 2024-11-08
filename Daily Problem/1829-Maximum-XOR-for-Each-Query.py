class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_num = 2 ** maximumBit - 1
        ans = []

        res = 0
        for num in nums:
            res ^= num

        for num in reversed(nums):
            ans.append(max_num ^ res)
            res ^= num

        return ans
