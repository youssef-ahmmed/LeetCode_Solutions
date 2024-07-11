class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        res = ""

        for b in s:
            if b == ')':
                portion = []
                while stack and stack[-1] != '(':
                    portion.append(stack.pop())
                stack.pop()

                stack.extend(portion)
            else:
                stack.append(b)

        return ''.join(stack)
