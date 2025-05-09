class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            m = l + (r - l) // 2
            s = (m * (m + 1)) // 2

            if s <= n:
                l = m + 1
            else:
                r = m - 1

        return l - 1
