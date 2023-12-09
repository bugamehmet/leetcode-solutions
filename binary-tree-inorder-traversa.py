def inorderTraversal(self, root):
    result = []
    if root:
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
    return result
