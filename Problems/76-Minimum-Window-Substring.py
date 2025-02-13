class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_size = float('inf')

        t_count = Counter(t)
        s_count = defaultdict(int)

        have, need = 0, len(t_count)

        save_st, st = 0, 0
        for en in range(len(s)):
            char = s[en]
            s_count[char] += 1

            if char in t_count and t_count[char] == s_count[char]:
                have += 1

            while have == need:
                if (en - st + 1) < min_size:
                    min_size = en - st + 1
                    save_st = st

                s_count[s[st]] -= 1
                if s[st] in t_count and s_count[s[st]] < t_count[s[st]]:
                    have -= 1

                st += 1

        return s[save_st : save_st + min_size] if min_size != float('inf') else \\