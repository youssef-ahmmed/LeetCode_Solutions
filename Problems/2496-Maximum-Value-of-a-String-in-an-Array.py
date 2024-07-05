class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        mx_val = 0

        for s in strs:
            if s.isdigit():
                mx_val = max(mx_val, int(s))
            else:
                mx_val = max(mx_val, len(s))

        return mx_val
