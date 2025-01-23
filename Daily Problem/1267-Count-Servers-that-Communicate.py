class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        row_cnt = [0] * m
        col_cnt = [0] * n

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_cnt[i] += 1
                    col_cnt[j] += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] and max(row_cnt[i], col_cnt[j]) > 1:
                    count += 1

        return count
