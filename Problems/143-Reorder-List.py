# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        \\\
        Do not return anything, modify head in-place instead.
        \\\
        def reverse(head: Optional[ListNode]):
            prev, cur = None, head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev, cur = cur, nxt

            return prev

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow
        second_half = reverse(mid.next)
        mid.next = None

        first_half = head
        while second_half:
            nxt1, nxt2 = first_half.next, second_half.next

            first_half.next = second_half
            second_half.next = nxt1

            first_half = nxt1
            second_half = nxt2
