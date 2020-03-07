# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def equal(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        elif not s and t:
            return False
        elif s and not t:
            return False

        if s.val != t.val:
            return False
        else:
            return self.equal(s.left, t.left) and self.equal(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        elif not s:
            return False

        if self.equal(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
