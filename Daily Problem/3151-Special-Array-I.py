class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for a, b in pairwise(nums):
            if a & 1 == b & 1:
                return False
        return True
