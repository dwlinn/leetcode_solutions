from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        queue = [root]
        result = [[root.val]]
        while not queue:
            n = len(queue)
            layer = [0] * n
            for i in range(n):
                node = queue.pop(0)
                layer[i] = node.val
                print(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(layer)
        return result