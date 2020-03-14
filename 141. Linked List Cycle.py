# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        x = head; y = head
        while y:
            x = x.next
            y = y.next
            if not y:
                return False
            else:
                y = y.next
            if x == y:
                return True
        return False
