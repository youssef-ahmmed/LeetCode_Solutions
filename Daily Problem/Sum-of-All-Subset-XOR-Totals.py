class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(start, sub):
            nonlocal total
            total += sub
            for i in range(start, len(nums)):
                sub ^= nums[i]
                backtrack(i + 1, sub)
                sub ^= nums[i]

        total = 0
        backtrack(0, 0)
        return total           
