class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def long_mono_subarray(op_func):
            curr = 1
            max_len = 1

            for i in range(1, len(nums)):
                if op_func(nums[i], nums[i - 1]):
                    curr += 1
                    max_len = max(max_len, curr)
                else:
                    curr = 1

            return max_len

        return max(long_mono_subarray(operator.gt), long_mono_subarray(operator.lt))
