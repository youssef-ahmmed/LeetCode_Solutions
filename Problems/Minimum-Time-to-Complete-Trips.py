class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 1, min(time) * totalTrips

        def can_do_faster(curr: int) -> bool:
            res = 0
            for t in time:
                res += curr // t
            return res >= totalTrips

        while l <= r:
            m = l + (r - l) // 2

            if can_do_faster(m):
                r = m - 1
            else:
                l = m + 1

        return l
