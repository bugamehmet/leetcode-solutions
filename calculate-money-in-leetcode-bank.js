// Calculate Money in Leetcode Bank

var totalMoney = function(n) {
  let total = 0;
  for (let i = 0; i < n; i++) {
      total += (i % 7) + 1 + Math.floor(i / 7);
  }
  return total;
};