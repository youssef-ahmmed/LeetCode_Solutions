class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n:
            return time + 1
        if (time // (n - 1)) & 1:
            return n - (time % (n - 1))
        return 1 + (time % (n - 1))
