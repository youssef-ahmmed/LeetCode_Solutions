class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        max_diff, max_num = 0, 0

        for num in nums:
            res = max(res, max_diff * num)
            max_diff = max(max_diff, max_num - num)
            max_num = max(max_num, num)

        return res
