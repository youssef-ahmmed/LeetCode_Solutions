class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        avgs = [-1] * n
        w_size = 2 * k + 1

        if w_size > n:
            return avgs

        w_sum = sum(nums[:w_size])

        for i in range(k, n - k):
            avgs[i] = w_sum // w_size
            if i + k + 1 < n:
                w_sum += nums[i + k + 1] - nums[i - k]

        return avgs
