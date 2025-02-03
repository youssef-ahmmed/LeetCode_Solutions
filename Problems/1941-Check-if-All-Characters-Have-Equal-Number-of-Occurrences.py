class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = Counter(s)
        values = list(count.values())

        for i in range(len(values) - 1):
            if values[i] != values[i + 1]:
                return False
        return True
