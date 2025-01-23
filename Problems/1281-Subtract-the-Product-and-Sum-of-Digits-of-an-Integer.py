class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1
        a = 0
        
        while n:
            a = n % 10
            n //= 10
            s += a
            p *= a

        return p - s
