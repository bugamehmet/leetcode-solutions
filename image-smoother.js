var imageSmoother = function(img) {
  const m = img.length;
  const n = img[0].length;
  const result = Array.from({ length: m }, () => Array(n).fill(0));
  const directions = [
      [0, 0], [0, 1], [0, -1],
      [1, 0], [1, 1], [1, -1],
      [-1, 0], [-1, 1], [-1, -1]
  ];

  for (let i = 0; i < m; i++) {
      for (let j = 0; j < n; j++) {
          let neighborSum = 0;
          let neighborCount = 0;

          for (const [dx, dy] of directions) {
              const x = i + dx;
              const y = j + dy;

              if (0 <= x && x < m && 0 <= y && y < n) {
                  neighborSum += img[x][y];
                  neighborCount++;
              }
          }

          result[i][j] = Math.floor(neighborSum / Math.max(1, neighborCount));
      }
  }

  return result;
}