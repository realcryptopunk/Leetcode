# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        slow.next = curr

        p1, p2 = head, prev
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        p1, p2 = head, prev
        while p2.next:
            next_node = p2.next
            p2.next = p1.next
            p1.next = p2
            p2 = next_node

        return True