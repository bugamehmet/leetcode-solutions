class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        expected_set = set(range(1, n * n + 1))
        actual_set = set()
        repeated = set()
        
        for i in range(n):
            for j in range(n):
                value = grid[i][j]
                if value in actual_set:
                    repeated.add(value)
                else:
                    actual_set.add(value)

        missing = (expected_set - actual_set).pop()
        return [repeated.pop(), missing]

"""class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        expected_set = set(range(1, n * n + 1))
        actual_set = set()

        repeated = {num for row in grid for num in row if num in actual_set or actual_set.add(num)}

        missing = (expected_set - actual_set).pop()
        return [repeated.pop(), missing]
"""