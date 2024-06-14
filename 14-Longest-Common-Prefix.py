class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = \\
        words = sorted(strs)
        first, last = words[0], words[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return common
            common += first[i]

        return common
