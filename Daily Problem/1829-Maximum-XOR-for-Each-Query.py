class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_num = 2 ** maximumBit - 1
        ans = []

        res = 0
        for num in nums:
            res ^= num

        for i in range(len(nums) - 1, -1, -1):
            k = max_num ^ res
            ans.append(k)
            res ^= nums[i]

        return ans
