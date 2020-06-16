Best solution.

```java
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(-1);
        ListNode curNode = head;

        while(l1!=null || l2!=null) {
            int val1 = (l1==null ? Integer.MAX_VALUE : l1.val);
            int val2 = (l2==null ? Integer.MAX_VALUE : l2.val);
            
            if(val1 < val2) {
                curNode.next = new ListNode(val1);
                l1 = l1.next;
            } else {
                curNode.next = new ListNode(val2);
                l2 = l2.next;
            }
            
            curNode = curNode.next;
        }
        
        return head.next;
    }
}
```

