class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for ch in s:
            if stack:
                if (stack[-1] == 'A' and ch == 'B') or (stack[-1] == 'C' and ch == 'D'):
                    stack.pop()
                else:
                    stack.append(ch)
            else:
                stack.append(ch)

        return len(stack)
