class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        count = {c: 0 for c in "abc"}

        st = 0
        for en in range(len(s)):
            count[s[en]] += 1

            while min(count.values()) > 0:
                count[s[st]] -= 1
                st += 1

            res += st

        return res
