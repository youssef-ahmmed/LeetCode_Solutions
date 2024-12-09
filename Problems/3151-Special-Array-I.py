class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        for x, y in pairwise(nums):
            if x & 1 == y & 1:
                return False
        return True
