// Check If Two String Arrays are Equivalent
// dizi.join('') === eşitse True değilse False döndürür
var arrayStringsAreEqual = function(word1, word2) {
  merge_1 = word1.join('')
  merge_2 = word2.join('')
  return merge_1 === merge_2
};

// başka bir çözüm
var arrayStringsAreEqual = function(word1, word2) {
  let b_1 = '';
  let b_2 = '';
  word1.forEach((i)=>{
    b_1 += i
  });
  word2.forEach((j)=>{
    b_2 += j
});
  return b_1 === b_2;
};