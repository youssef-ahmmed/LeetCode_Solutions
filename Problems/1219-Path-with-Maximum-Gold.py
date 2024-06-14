class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def backtrack(r, c, visit):
            if (
                min(r, c) < 0 or r == rows or c == cols or
                grid[r][c] == 0 or (r, c) in visit
            ):
                return 0

            res = grid[r][c]
            visit.add((r, c))
            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for r1, c1 in neighbors:
                res = max(res, grid[r][c] + backtrack(r1, c1, visit))

            visit.remove((r, c))

            return res

        gold = 0
        for i in range(rows):
            for j in range(cols):
                gold = max(gold, backtrack(i, j, set()))

        return gold
