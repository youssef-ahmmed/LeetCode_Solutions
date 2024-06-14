class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        max_local = []
        sz = len(grid)

        for i in range(sz - 2):
            temp_row = []
            for j in range(sz - 2):
                mx_loc = float('-inf')
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        mx_loc = max(mx_loc, grid[k][l])
                temp_row.append(mx_loc)
            max_local.append(temp_row)

        return max_local
