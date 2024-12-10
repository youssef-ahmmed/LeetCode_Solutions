class Solution:
    def maximumLength(self, s: str) -> int:
        count = defaultdict(int)

        k = 1
        while k <= len(s):
            for i in range(len(s) - k + 1):
                count[s[i: i + k]] += 1
            k += 1

        values = [key for key, value in count.items()
        if value >= 3 and len(set(key)) == 1]

        return len(max(values, key=len)) if values else -1
