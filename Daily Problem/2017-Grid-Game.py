class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        pre0, pre1 = [0] * n, [0] * n
        pre0[0], pre1[0] = grid[0][0], grid[1][0]

        for i in range(1, n):
            pre0[i] = pre0[i - 1] + grid[0][i]
            pre1[i] = pre1[i - 1] + grid[1][i]

        min_score = float("inf")
        for t in range(n):
            top = pre0[-1] - pre0[t]
            bottom = pre1[t - 1] if t > 0 else 0
            robot2_score = max(top, bottom)
            min_score = min(min_score, robot2_score)

        return min_score
