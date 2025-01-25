class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        seen = set()

        st = 0
        for en, num in enumerate(nums):
            while num in seen:
                curr -= nums[st]
                seen.remove(nums[st])
                st += 1
            seen.add(nums[en])
            curr += nums[en]
            res = max(res, curr)

        return res
