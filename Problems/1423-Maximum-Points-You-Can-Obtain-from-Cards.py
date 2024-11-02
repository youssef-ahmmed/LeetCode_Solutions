class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = defaultdict(int)
        max_occurr = 0

        for i in range(len(s) - minSize + 1):
            sub = s[i:i + minSize]

            if len(set(sub)) <= maxLetters:
                freq[sub] += 1
                max_occurr = max(max_occurr, freq[sub])

        return max_occurr
