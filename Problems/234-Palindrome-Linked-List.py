# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(h):
            prev, cur = None, h

            while cur:
                nxt = cur.next
                cur.next = prev
                prev, cur = cur, nxt

            return prev

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = reverse(slow)

        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True
