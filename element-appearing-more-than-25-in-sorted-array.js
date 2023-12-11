var findSpecialInteger = function(arr) {
  let count = 1;
  const time = Math.floor(arr.length / 4) + 1;

  for (let i = 0; i < arr.length - 1; i++) {
      if (arr[i] === arr[i + 1]) {
          count += 1;
          if (count >= time) {
              return arr[i];
          }
      } else {
          count = 1;
      }
  }

  return arr[arr.length - 1]; // listenin son elemanına ulaşır.
};