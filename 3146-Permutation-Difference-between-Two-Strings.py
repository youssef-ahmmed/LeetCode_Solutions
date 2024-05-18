class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        cnt = 0
        for ch in s:
            cnt += abs(s.index(ch) - t.index(ch))

        return cnt
