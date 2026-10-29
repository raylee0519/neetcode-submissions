class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast = head
        faster = head

        while faster and faster.next:
            fast = fast.next
            faster = faster.next.next

            if fast == faster:
                return True

        return False