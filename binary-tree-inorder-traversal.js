// 94. Binary Tree Inorder Traversal
/**
let dizi1 = [1, 2, 3];
let dizi2 = [4, 5, 6];

let birlesikDizi = dizi1.concat(dizi2);

console.log(birlesikDizi);  // Çıktı: [1, 2, 3, 4, 5, 6]
console.log(dizi1);         // Çıktı: [1, 2, 3] (değişmemiş)
console.log(dizi2);         // Çıktı: [4, 5, 6] (değişmemiş)
 */


var inorderTraversal = function(root) {
  let result = [];
  if(root){
      result = result.concat(inorderTraversal(root.left));
      result.push(root.val);
      result = result.concat(inorderTraversal(root.right));
  };
  return result;
};