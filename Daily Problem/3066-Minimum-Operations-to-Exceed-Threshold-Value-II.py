from heapq import *

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x, y, m, oper = 0, 0, 0, 0

        heapify(nums)

        if nums[0] >= k:
            return 0

        while k > m:
            x, y = heappop(nums), heappop(nums)
            res = 2 * min(x, y) + max(x, y)
            heappush(nums, res)
            m = nums[0]
            oper += 1

        return oper
