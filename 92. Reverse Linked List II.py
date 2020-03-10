# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if(m == n):
            return head

        if m > 1:
            beginLeft = head
            for i in range(m - 2):
                beginLeft = beginLeft.next
            left = beginLeft.next
        else:
            left = head

        begin = left
        right = left.next
        prev = None
        for i in range(n - m + 1):
            left.next = prev
            prev = left
            if i != n - m:
                left = right
                right = right.next
        begin.next = right
        
        if m > 1:
            beginLeft.next = left
        else:
            head = left
        begin.next = right
        return head
