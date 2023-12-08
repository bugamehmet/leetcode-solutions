// Construct String from Binary Tree

var tree2str = function(root) {
  if(root == null){
    return ""
  }
  result = String(root.val)

  if(root.left || root.right){
    result += `(${tree2str(root.left)})`
  }
  if(root.right){
    result += `(${tree2str(root.right)})`  }
  return result
};
