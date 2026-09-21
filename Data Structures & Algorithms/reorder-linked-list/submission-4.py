class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        # 1. 중간 지점 찾기
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 뒤 절반 reverse
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 3. 앞/뒤 리스트 merge
        node1 = head
        node2 = prev

        while node2:
            node1_next = node1.next
            node2_next = node2.next

            node1.next = node2
            node2.next = node1_next

            node1 = node1_next
            node2 = node2_next