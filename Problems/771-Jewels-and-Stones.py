class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for j in jewels:
            res += stones.count(j)

        return res
