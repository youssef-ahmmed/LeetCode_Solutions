class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(cap: int) -> bool:
            res = 1
            curr = 0
            for w in weights:
                if curr + w > cap:
                    curr = w
                    res += 1
                else:
                    curr += w
            return res <= days

        l, r = max(weights), sum(weights)

        while l < r:
            m = l + (r - l) // 2

            if can_ship(m):
                r = m
            else:
                l = m + 1

        return l
