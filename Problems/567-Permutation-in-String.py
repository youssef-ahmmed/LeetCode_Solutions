class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, k = len(s2), len(s1)
        s1_count = Counter(s1)
        s2_count = Counter(s2[:k])
        
        if s1_count == s2_count:
            return True

        for i in range(k, n):
            s2_count[s2[i]] += 1
            s2_count[s2[i - k]] -= 1
            if s2_count[s2[i - k]] == 0:
                del s2_count[s2[i - k]]

            if s1_count == s2_count:
                return True

        return False
