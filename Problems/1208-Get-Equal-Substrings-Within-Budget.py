class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Maximum Length from `s` that can be changed to equal `t` within `maxCost`
        st = 0
        curr, max_len = 0, 0

        for en in range(len(s)):
            curr += abs(ord(t[en]) - ord(s[en]))

            while curr > maxCost:
                curr -= abs(ord(t[st]) - ord(s[st]))
                st += 1

            max_len = max(max_len, en - st + 1)

        return max_len
