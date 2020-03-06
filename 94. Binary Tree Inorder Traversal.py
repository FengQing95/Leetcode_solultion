# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.traverse(root, res)
        return res

    def traverse(self, cur, res):
        if cur:
            self.traverse(cur.left, res)
            res.append(cur.val)
            self.traverse(cur.right, res)
