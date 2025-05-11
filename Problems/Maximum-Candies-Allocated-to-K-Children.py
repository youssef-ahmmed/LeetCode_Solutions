class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can_divide(p: int) -> bool:
            res = 0
            for c in candies:
                res += c // p
            return res >= k

        l, r = 1, max(candies) + 1

        while l < r:
            m = l + (r - l) // 2

            if can_divide(m):
                l = m + 1
            else:
                r = m
            
        return l - 1
