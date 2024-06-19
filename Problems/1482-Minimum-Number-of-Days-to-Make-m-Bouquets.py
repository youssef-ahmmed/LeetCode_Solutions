class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        l, r = min(bloomDay), max(bloomDay)

        def canMakeBouquets(d: int):
            flowers = 0
            bouquets = 0

            for day in bloomDay:
                if d >= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                        if bouquets == m:
                            return True
                else:
                    flowers = 0

            return bouquets >= m

        while l < r:
            d = l + (r - l) // 2

            if canMakeBouquets(d):
                r = d
            else:
                l = d + 1

        return l
