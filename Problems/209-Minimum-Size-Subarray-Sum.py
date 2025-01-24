class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float(\inf\)
        curr = 0
        s = 0

        for e in range(len(nums)):
            curr += nums[e]

            while curr >= target:
                min_len = min(min_len, e - s + 1)
                curr -= nums[s]
                s += 1

        return min_len if min_len != float(\inf\) else 0
