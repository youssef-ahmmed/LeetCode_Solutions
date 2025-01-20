class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        freq = [[0] * (m + 1) for _ in range(n + 1)]

        map_idx = {}
        for i in range(n):
            for j in range(m):
                map_idx[mat[i][j]] = (i, j)

        for i in range(n * m):
            row = map_idx[arr[i]][0]
            col = map_idx[arr[i]][1]
            freq[row][col] = 1

            # how to check that row or column is completely painted
            freq[row][m] += 1
            freq[n][col] += 1
            if freq[row][m] == m or freq[n][col] == n:
                return i

        return 0
