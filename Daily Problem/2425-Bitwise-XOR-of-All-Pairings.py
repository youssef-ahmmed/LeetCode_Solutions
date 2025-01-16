class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        len1, len2 = len(nums1), len(nums2)
        
        if len1 % 2 == 0 and len2 % 2 == 0:
            return 0
        
        if len1 % 2 != 0:
            for n in nums2:
                res ^= n
        
        if len2 % 2 != 0:
            for n in nums1:
                res ^= n
        
        return res
