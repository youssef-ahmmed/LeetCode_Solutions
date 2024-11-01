class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ''
        
        for c in s:
            if len(ans) < 2 or ans[-1] != c or ans[-2] != c:
                ans += c

        return ans
