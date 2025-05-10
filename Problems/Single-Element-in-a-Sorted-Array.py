class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        def is_neighbor(idx: int) -> bool:
            return nums[idx] == nums[idx ^ 1]

        while l < r:
            m = l + (r - l) // 2

            if is_neighbor(m):
                l = m + 1
            else:
                r = m

        return nums[l]
