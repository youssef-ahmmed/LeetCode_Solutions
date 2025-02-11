class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)

        for c in s:
            stack.append(c)

            if len(stack) >= part_len and ''.join(stack[-part_len:]) == part:
                del stack[-part_len:]

        return ''.join(stack)
