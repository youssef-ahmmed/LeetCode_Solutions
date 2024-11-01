class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = defaultdict(int)

        for i in range(len(s) - minSize + 1):
            sub = s[i:i + minSize]
            if len(set(sub)) <= maxLetters:
                freq[sub] += 1

        return max(freq.values()) if freq else 0
