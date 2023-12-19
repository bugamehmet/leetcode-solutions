class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]

        directions = [(0, 0), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]

        for i in range(m):
            for j in range(n):
                neighbors_sum, neighbors_count = 0, 0

                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n:
                        neighbors_sum += img[x][y]
                        neighbors_count += 1

                result[i][j] = neighbors_sum // neighbors_count

        return result