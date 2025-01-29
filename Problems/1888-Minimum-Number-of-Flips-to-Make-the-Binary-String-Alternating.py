class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        double = 2 * s

        alt1 = "".join(['1' if i % 2 == 0 else '0' for i in range(2 * n)])
        alt2 = "".join(['0' if i % 2 == 0 else '1' for i in range(2 * n)])

        diff1, diff2 = 0, 0
        min_flips = len(double)

        l = 0
        for r in range(2 * n):
            if double[r] != alt1[r]:
                diff1 += 1
            if double[r] != alt2[r]:
                diff2 += 1

            if (r - l + 1) > n:
                if double[l] != alt1[l]:
                    diff1 -= 1
                if double[l] != alt2[l]:
                    diff2 -= 1
                l += 1

            if (r - l + 1) == n:
                min_flips = min(min_flips, diff1, diff2)

        return min_flips
