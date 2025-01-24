class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_count = 0
        max_len = 0
        start = 0

        for end in range(len(s)):
            count[s[end]] += 1
            max_count = max(max_count, count[s[end]])

            while (end - start + 1) - max_count > k:
                count[s[start]] -= 1
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
