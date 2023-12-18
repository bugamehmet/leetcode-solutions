var maxProductDifference = function(nums) {
  let min1 = min2 = Infinity
  let max1 = max2 = 0

  nums.forEach(num => {
      // En küçük değerleri güncelle
      if (num < min1) {
          min2 = min1;
          min1 = num;
      } else if (num < min2) {
          min2 = num;
      }

      // En büyük değerleri güncelle
      if (num > max1) {
          max2 = max1;
          max1 = num;
      } else if (num > max2) {
          max2 = num;
      }
  });
  return (max1 * max2) - (min1 * min2)
};