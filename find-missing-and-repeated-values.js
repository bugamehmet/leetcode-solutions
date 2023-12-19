var findMissingAndRepeatedValues = function(grid) {
  const n = grid.length;
  const vec = Array(n * n + 1).fill(0);
  let a, b;

  for (let row of grid) {
      for (let num of row) {
          vec[num]++;
      }
  }

  for (let i = 1; i <= n * n; i++) {
      if (vec[i] === 2) {
          a = i;
      }
      if (vec[i] === 0) {
          b = i;
      }
  }

  return [a, b];
};
