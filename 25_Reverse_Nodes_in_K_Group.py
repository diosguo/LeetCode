# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        stack = list()

        t = ListNode(0)
        t.next = head
        res_t = t
        pre_stop = False
        p = head
        while p:
            for i in range(k):
                if p:
                    stack.append(p)
                    p = p.next
                else:
                    pre_stop = True
                    break

            if not pre_stop:
                for i in range(k):
                    res_t.next = stack.pop(-1)
                    res_t = res_t.next
            else:
                for i in stack:
                    res_t.next = i
                    res_t = res_t.next
            res_t.next = None
        return t.next


a = ListNode(1)
a.next = ListNode(2)
s = Solution()
res = s.reverseKGroup(a,2)

while res:
    print(res.val)
    res = res.next