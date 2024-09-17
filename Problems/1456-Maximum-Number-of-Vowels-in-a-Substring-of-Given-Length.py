class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        cnt = 0
        vowels = 'aeiou'

        for i in range(k):
            if s[i] in vowels:
                cnt += 1

        mx = cnt
        for i in range(k, len(s)):
            if s[i] in vowels:
                cnt += 1
            if s[i - k] in vowels:
                cnt -= 1

            mx = max(mx, cnt)

        return mx
