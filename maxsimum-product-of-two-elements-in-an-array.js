var maxProduct = function(nums) {
  let max1 = -1;
  let max2 = -1;

  for (let i = 0; i < nums.length; i++) {
      if (nums[i] >= max1) {
          max2 = max1;
          max1 = nums[i];
      } else if (nums[i] > max2) {
          max2 = nums[i];
      }
  }

  return (max1 - 1) * (max2 - 1);
};
