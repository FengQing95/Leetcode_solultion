# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def equal(self, node1, node2):
        if not node1 and node2:
            return True
        elif not node1 or not node2:
            return False
        else:
            return node1.val == node2.val

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSymmetric2(root.left, root.right)

    def isSymmetric2(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        
        if not self.equal(node1, node2):
            return False
        else:
            return self.isSymmetric2(node1.left, node2.right) and self.isSymmetric2(node2.left, node1.right)
