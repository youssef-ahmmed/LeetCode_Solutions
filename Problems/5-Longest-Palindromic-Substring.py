class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand_around_center(l, r):
            nonlocal max_len, palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    palindrome = s[l:r + 1]
                l -= 1
                r += 1

        palindrome = \\
        max_len = 0

        for i in range(len(s)):
            expand_around_center(i, i)
            expand_around_center(i, i + 1)

        return palindrome
