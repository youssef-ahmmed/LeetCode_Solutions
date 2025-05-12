class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 1, num

        while l < r:
            m = l + (r - l) // 2
            double = m * m

            if double == num:
                return True

            if double < num:
                l = m + 1
            else:
                r = m

        return False
        