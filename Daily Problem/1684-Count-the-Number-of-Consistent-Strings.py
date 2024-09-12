class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        cnt = 0

        for word in words:
            if all(char in allowed for char in word):
                cnt += 1

        return cnt
