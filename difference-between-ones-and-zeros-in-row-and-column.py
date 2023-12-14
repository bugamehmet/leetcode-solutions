class Solution:
    def onesMinusZeros(self, grid):
        rows, cols = len(grid), len(grid[0])

        row_sum = [0] * rows
        col_sum = [0] * cols

        for i in range(rows):
            for j in range(cols):
                row_sum[i] += grid[i][j]
                col_sum[j] += grid[i][j]

        for i in range(rows):
            for j in range(cols):
                grid[i][j] = 2 * (row_sum[i] + col_sum[j]) - rows - cols

        return grid
    

"""
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        def get_rows_sum(row_idx):
            result = 0
            for i in range(len(row_idx)):
                if row_idx[i] == 0:
                    result += -1
                else:
                    result += 1
            return result

        def get_col_sum(col_idx):
            result = 0
            for i in range(len(col_idx)):
                if col_idx[i] == 0:
                    result += -1
                else:
                    result += 1
            return result
        
        diff = []
        for row in grid:
            row_sum = get_rows_sum(row)
            row_diff = []
            for col_idx in zip(*grid):
                col_sum = get_col_sum(col_idx)
                sum_row_col = row_sum + col_sum
                row_diff.append(sum_row_col)
            diff.append(row_diff)

        return diff
"""