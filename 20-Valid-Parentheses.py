class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { ')': '(', '}': '{', ']': '[' }
        stack = []

        for b in s:
            if b in brackets.values():
                stack.append(b)
            elif stack and stack[-1] == brackets[b]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
