class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        cnt = numBottles

        while numBottles >= numExchange:
            exchange = numBottles // numExchange
            remainder = numBottles % numExchange

            cnt += exchange

            numBottles = exchange + remainder

        return cnt
