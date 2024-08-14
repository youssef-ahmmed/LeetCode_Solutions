class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        l, r = 0, nums[-1] - nums[0]

        def helper(dist):
            l = 0
            count = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > dist:
                    l += 1
                count += r - l

            return count

        while l < r:
            mid = l + ((r - l) // 2)
            if helper(mid) >= k:
                r = mid
            else:
                l = mid + 1

        return l
