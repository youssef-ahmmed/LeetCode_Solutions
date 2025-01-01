class Solution:
    def maxScore(self, s: str) -> int:
        zero = 0
        one = s.count('1')
        score = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zero += 1
            else:
                one -= 1

            score = max(score, one + zero)

        return score
