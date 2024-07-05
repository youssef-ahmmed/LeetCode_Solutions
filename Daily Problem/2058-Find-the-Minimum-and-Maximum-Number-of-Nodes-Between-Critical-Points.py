# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical_idx = []

        prev, cur = head, head.next
        idx = 1

        while cur.next:
            nxt = cur.next
            if ((cur.val > prev.val and cur.val > nxt.val)
                or
                (cur.val < prev.val and cur.val < nxt.val)):
                critical_idx.append(idx)
            idx += 1
            prev = cur
            cur = cur.next

        if len(critical_idx) <= 1:
            return [-1, -1]

        min_dis = float('inf')

        for i in range(1, len(critical_idx)):
            min_dis = min(min_dis, critical_idx[i] - critical_idx[i - 1])

        max_dis = critical_idx[-1] - critical_idx[0]

        return [min_dis, max_dis]
