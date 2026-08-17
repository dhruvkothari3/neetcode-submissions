class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Reverse
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Remove nth node
        curr = prev

        if n == 1:
            prev = prev.next
        else:
            for i in range(n - 2):
                curr = curr.next

            curr.next = curr.next.next

        # Reverse again
        curr = prev
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev