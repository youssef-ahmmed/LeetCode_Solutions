class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        w_sum = max_sum = 0
        count = Counter()
        dist_count = 0

        l = 0
        for r in range(n):
            w_sum += nums[r]
            count[nums[r]] += 1
            if count[nums[r]] == 1:
                dist_count += 1
            elif count[nums[r]] == 2:
                dist_count -= 1

            if r - l + 1 > k:
                w_sum -= nums[l]
                count[nums[l]] -= 1
                if count[nums[l]] == 1:
                    dist_count += 1
                elif count[nums[l]] == 0:
                    dist_count -= 1
                l += 1

            if r - l + 1 == k and dist_count == k:
                max_sum = max(max_sum, w_sum)

        return max_sum