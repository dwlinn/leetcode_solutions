from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root:
            result.append(root.val)
        if root.left:
            self.inorderTraversal(root.left)
        if root.right:
            self.inorderTraversal(root.right)
        return result
        