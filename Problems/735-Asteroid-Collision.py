class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                top = stack[-1]
                if top == -ast:
                    stack.pop()
                    break
                elif top > -ast:
                    break
                else:
                    stack.pop()
                    continue
            else:
                stack.append(ast)

        return stack
