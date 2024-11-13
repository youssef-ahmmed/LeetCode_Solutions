class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def bin_search(l, r, target):
            while l <= r:
                m = (l + r) // 2
                if nums[m] >= target:
                    r = m - 1
                else:
                    l = m + 1

            return r
        
        n = len(nums)
        count = 0
        nums.sort()

        for i in range(len(nums)):
            up = upper - nums[i]
            low = lower - nums[i]

            count += (
                bin_search(i + 1, n - 1, up + 1) -
                bin_search(i + 1, n - 1, low)
            )

        return count
