class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row_sz = len(grid)
        col_sz = len(grid[0])

        def calculate_score(matrix):
            total_sum = 0
            for row in matrix:
                bin_string = ''.join(map(str, row))
                number = int(bin_string, 2)
                total_sum += number

            return total_sum

        for i in range(row_sz):
            binary_string = ''.join(map(str, grid[i]))
            num = int(binary_string, 2)
            flipped_num = num ^ ((1 << col_sz) - 1)
            if flipped_num > num:
                grid[i] = [bit ^ 1 for bit in grid[i]]

        for j in range(col_sz):
            one_cnt = 0
            for i in range(row_sz):
                one_cnt += grid[i][j]

            if one_cnt < row_sz - one_cnt:
                for r in range(row_sz):
                    grid[r][j] = 0 if grid[r][j] else 1

        return calculate_score(grid)