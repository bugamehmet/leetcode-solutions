var onesMinusZeros = function(grid) {
  const rows = grid.length;
  const cols = grid[0].length;

  const rowSum = Array(rows).fill(0);
  const colSum = Array(cols).fill(0);

  for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
          rowSum[i] += grid[i][j];
          colSum[j] += grid[i][j];
      }
  }

  for (let i = 0; i < rows; i++) {
      for (let j = 0; j < cols; j++) {
          grid[i][j] = 2 * (rowSum[i] + colSum[j]) - rows - cols;
      }
  }

  return grid;
};
