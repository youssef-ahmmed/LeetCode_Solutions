class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1

        if target > nums[-1]:
            return n

        while l < r:
            m = l + (r - l) // 2

            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m
        
        return l
