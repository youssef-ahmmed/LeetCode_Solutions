class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        prefix_sum = [0] * n
        postfix_sum = [0] * n

        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        postfix_sum[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            postfix_sum[i] = postfix_sum[i + 1] + nums[i]

        for i in range(n):
            left_sum = prefix_sum[i - 1] if i > 0 else 0
            right_sum = postfix_sum[i + 1] if i < n - 1 else 0

            if left_sum == right_sum:
                return i

        return -1
