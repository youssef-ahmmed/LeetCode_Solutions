class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(sqrt(c))

        while l <= r:
            result =  l * l + r * r
            if result == c:
                return True
            elif result > c:
                r -= 1
            else:
                l += 1

        return False
