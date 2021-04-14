class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        b_head = b = ListNode()
        a_head = a = ListNode()
        while head:
            if head.val < x:
                a.next = head
                a = a.next
            else:
                b.next = head
                b = b.next
            head = head.next
        b.next = None
        a.next = b_head.next
        return a_head.next