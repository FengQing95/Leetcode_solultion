# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        if not head:
            return head
        else:
            stack = []
            cur = head
            res = ListNode(-1); cur_res = res
            while cur:
                stack.append(cur.val)
                cur = cur.next
            for i in reversed(stack):
                cur_res.next = ListNode(i)
                cur_res = cur_res.next
            return res.next
