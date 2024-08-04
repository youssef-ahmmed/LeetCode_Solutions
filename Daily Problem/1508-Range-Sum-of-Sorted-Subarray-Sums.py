class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sum_subarrays = []

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                sum_subarrays.append(s)

        sum_subarrays.sort()

        return sum(sum_subarrays[left - 1:right]) % (10 ** 9 + 7)
