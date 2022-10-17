#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   86_分隔链表.py
@Time    :   2022/10/18 00:28:32
@Author  :   DiosGuo 
@Version :   1.0
@Contact :   raogx.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        little_list_root = ListNode()
        big_list_root = ListNode() 

        p = head
        l_p, b_p = little_list_root, big_list_root  
        while p:
            if p.val < x:
                l_p.next = p
                p = p.next 
                l_p = l_p.next 
                l_p.next = None 
            else:
                b_p.next = p 
                p = p.next 
                b_p = b_p.next 
                b_p.next = None 
            # p = p.next 

        # 合并
        if big_list_root.next:
            l_p.next = big_list_root.next 
        return little_list_root.next  


if __name__ == '__main__':
    data = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
    s = Solution() 
    res = s.partition(data, 3) 

    while res:
        print(res.val) 
        res = res.next
    # print(s.partition(data, 3).val)
