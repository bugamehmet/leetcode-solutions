/**
 * @param {string} s
 * @return {number}
 */
var minOperations = function(s) {
  let startChar = "0";
  let operations = 0;

  for (let i = 0; i < s.length; i++) {
      if (s[i] === startChar) {
          operations++;
      }

      startChar = startChar === "1" ? "0" : "1";
  }

  return Math.min(operations, s.length - operations);
};