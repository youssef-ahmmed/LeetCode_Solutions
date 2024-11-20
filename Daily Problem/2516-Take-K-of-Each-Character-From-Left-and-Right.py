class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = {'a': 0, 'b': 0, 'c': 0}
        for c in s:
            total[c] += 1

        if min(total.values()) < k:
            return -1

        mx_size = 0
        l = 0
        n = len(s)
        for r in range(n):
            total[s[r]] -= 1

            while min(total.values()) < k:
                total[s[l]] += 1
                l += 1

            mx_size = max(mx_size, r - l + 1)

        return n - mx_size
