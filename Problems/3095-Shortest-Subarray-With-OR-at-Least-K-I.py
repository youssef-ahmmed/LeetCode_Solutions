class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_len = 51
        n = len(nums)

        for i in range(n):
            res = 0
            for j in range(i, n):
                res |= nums[j]
                if res >= k:
                    min_len = min(min_len, j - i + 1)
                    break

        return -1 if min_len == 51 else min_len                
