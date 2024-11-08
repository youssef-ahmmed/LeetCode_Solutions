class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        n = len(s)

        if k > n:
            return []

        p_count = defaultdict(int)
        s_count = defaultdict(int)

        for c in p:
            p_count[c] += 1

        for i in range(len(p)):
            s_count[s[i]] += 1

        res = []
        if p_count == s_count:
            res.append(0)

        for i in range(k, n):
            s_count[s[i]] += 1
            s_count[s[i - k]] -= 1

            if s_count[s[i - k]] == 0:
                s_count.pop(s[i - k])

            if p_count == s_count:
                res.append(i - k + 1)

        return res
