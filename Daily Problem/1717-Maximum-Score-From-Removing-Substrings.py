class Solution:
    def remove_pairs(self, pair: str, score: int) -> int:
        res = 0
        stack = []

        for c in self.s:
            if stack and c == pair[1] and stack[-1] == pair[0]:
                res += score
                stack.pop()
            else:
                stack.append(c)

        self.s = ''.join(stack)

        return res

    def maximumGain(self, s: str, x: int, y: int) -> int:
        self.s = s
      
        score = 0
        pair = "ab" if x > y else "ba"
        
        score += self.remove_pairs(pair, max(x, y))
        score += self.remove_pairs(pair[::-1], min(x, y))

        return score
