class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0

        while l <= r:
            m = l + (r - l) // 2
            double = m ** 2
            if double == x:
                return m
            elif double < x:
                l = m + 1
                res = m
            else:
                r = m - 1

        return res
