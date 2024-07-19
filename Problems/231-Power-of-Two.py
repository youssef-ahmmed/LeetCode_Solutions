class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return 2 ** math.floor(math.log(n, 2)) == n
