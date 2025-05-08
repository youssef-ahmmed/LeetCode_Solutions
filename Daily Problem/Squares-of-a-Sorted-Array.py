class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        res = [0] * n

        while n:
            n -= 1
            if abs(nums[i]) < abs(nums[j]):
                res[n] = nums[j] * nums[j]
                j -= 1
            else:
                res[n] = nums[i] * nums[i]
                i += 1

        return res
