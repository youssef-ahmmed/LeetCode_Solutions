class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_str = ''

        j = 0
        for i, c in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                new_str += ' '
                j += 1
            new_str += c

        return new_str
