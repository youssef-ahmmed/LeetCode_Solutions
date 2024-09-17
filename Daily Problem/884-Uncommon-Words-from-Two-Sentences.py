class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        uncommon = []

        s1_ocurr = Counter(s1.split())
        s2_ocurr = Counter(s2.split())

        for k, v in s1_ocurr.items():
            if v == 1 and not s2_ocurr.get(k):
                uncommon.append(k)

        for k, v in s2_ocurr.items():
            if v == 1 and not s1_ocurr.get(k):
                uncommon.append(k)

        return uncommon
