# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visited_node_set = set() 

        pos = -1 
        p = head 
        while p:
            if p in visited_node_set:
                return True 
            else:
                visited_node_set.add(p) 
                p = p.next
        
        return False