# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        move = head
        num = 0
        while move :
            move = move.next
            num += 1
        delete = num - n
        num = 0

        while head :
            if num == delete : 
                prev.next = head.next
                break
            head = head.next
            prev = prev.next
            num += 1
    
        return dummy.next
        