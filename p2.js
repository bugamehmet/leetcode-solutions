// Count of Matches in Tournament
// Math.floor tam sayı yapmak için
var numberOfMatches = function(n) {
  let teams = n;
  let sum = 0;
  while (teams > 1) {
      if (teams % 2 == 0) {
          sum += Math.floor(teams / 2);
          teams = teams / 2;
      } else {
          sum += Math.floor((teams - 1) / 2);
          teams = (teams - 1) / 2 + 1;
      }
  }
  return sum;
};
