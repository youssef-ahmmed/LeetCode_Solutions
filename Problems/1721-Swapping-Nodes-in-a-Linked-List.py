# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        from_start, from_end = None, head
        R = head

        for i in range(k):
            from_start = R
            R = R.next

        while R:
            from_end = from_end.next
            R = R.next

        from_start.val, from_end.val = from_end.val, from_start.val

        return head