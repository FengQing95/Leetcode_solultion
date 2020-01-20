 Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        
        cur1 = l1; cur2 = l2
        res = ListNode(-1); cur = res
        while cur1 or cur2:
            if not cur1 or (cur2 and cur1.val > cur2.val):
                cur.next = ListNode(cur2.val)
                cur2 = cur2.next
            else:
                cur.next = ListNode(cur1.val)
                cur1 = cur1.next
            cur = cur.next     
        
        return res.next
