class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        count = defaultdict(int)
        max_len = 0

        for end in range(len(s)):
            count[s[end]] += 1

            while end - start + 1 > len(count):
                count[s[start]] -= 1
                if count[s[start]] == 0:
                    del count[s[start]]
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
