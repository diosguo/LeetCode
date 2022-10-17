"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]

输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-k-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from queue import PriorityQueue 
from typing import Optional, List 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Elem:
    def __init__(self, node) -> None:
        self.node = node
    
    def __lt__(self, other):
        
        if self.node.val < other.val:
            return True 
        else:
            return False 


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = PriorityQueue() 

        new_list = ListNode() 

        p = new_list

        for t in lists:
            if t is not None:
                queue.put(Elem(t))

        while queue:
            min_info = queue.get()
            if min_info.node.next:
                queue.put(min_info.node.next.val, min_info.node.next) 
            p.next = min_info.node
            p = p.next
        
        return new_list.next
            
            
