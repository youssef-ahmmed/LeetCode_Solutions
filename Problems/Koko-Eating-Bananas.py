class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k: int) -> bool:
            res = 0
            for p in piles:
                res += ceil(p / k)
            return res <= h

        l, r = 1, max(piles)
    
        while l <= r:
            m = l + (r - l) // 2

            if can_eat(m):
                r = m - 1
            else:
                l = m + 1

        return l
