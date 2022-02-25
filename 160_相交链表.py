class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        if not headA or not headB:
            return None
        
        p1 = headA
        p2 = headB
        p1, p2 = headA, headB
        while p1 is not p2:
            if p1 == p2:
                return p1 

            p1 = headB if p1 is None else p1.next
            p2 = headA if p2 is None else p2.next

            



