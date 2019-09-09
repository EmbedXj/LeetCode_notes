# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(-1)
        highBit = 0
        pr = res
        while l1 or l2 or highBit == 1:
            pr.next = ListNode(-1)
            curBitRaw = (l1.val if l1 else 0) + (l2.val if l2 else 0) + highBit
            highBit = int(curBitRaw / 10)
            pr.next.val = curBitRaw % 10
            pr = pr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return res.next
