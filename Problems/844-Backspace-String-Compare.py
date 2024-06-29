class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []

        for ch in s:
            if stack_s and ch == '#':
                stack_s.pop()
            elif not stack_s and ch == '#':
                continue
            else:
                stack_s.append(ch)

        for ch in t:
            if stack_t and ch == '#':
                stack_t.pop()
            elif not stack_t and ch == '#':
                continue
            else:
                stack_t.append(ch)

        return stack_s == stack_t
