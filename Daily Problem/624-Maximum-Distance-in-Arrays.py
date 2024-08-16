class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn = arrays[0][0]
        mx = arrays[0][-1]
        max_dist = 0

        for i in range(1, len(arrays)):
            max_dist = max(max_dist, arrays[i][-1] - mn, mx - arrays[i][0])

            mn = min(mn, arrays[i][0])
            mx = max(mx, arrays[i][-1])

        return max_dist