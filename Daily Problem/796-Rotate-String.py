class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)

        if len(s) != len(goal):
            return False

        for i in range(n):
            if goal[i] == s[0]:
                if ((s[:i] == goal[n - i:] and s[i:] == goal[:n - i])
                    or (goal[:i] == s[n - i:] and goal[i:] == s[:n - i])):
                    return True
        
        return False
