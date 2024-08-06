class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        
        res, a = 0, 1

        while n > 0:
            if n // 8 >= 1:
                res += 8 * a
            else:
                res += n * a

            a += 1
            n -= 8

        return res
