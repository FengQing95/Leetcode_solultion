# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def add(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        else:
            newNode = TreeNode((t1.val if t1 else 0) +
                               (t2.val if t2 else 0))
            return newNode

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        newRoot = self.add(t1, t2)
        if newRoot:
            newRoot.left = self.mergeTrees(t1.left if t1 else None,
                                           t2.left if t2 else None)
            newRoot.right = self.mergeTrees(t1.right if t1 else None,
                                            t2.right if t2 else None)
        return newRoot
