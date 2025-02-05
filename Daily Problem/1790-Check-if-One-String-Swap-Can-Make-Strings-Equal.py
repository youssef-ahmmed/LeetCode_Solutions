class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diffs = [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]

        return not diffs or (len(diffs) == 2 
                            and s1[diffs[0]] == s2[diffs[1]]
                            and s1[diffs[1]] == s2[diffs[0]])
