#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   1656_设计有序流.py
@Time    :   2022/08/16 23:48:46
@Author  :   DiosGuo 
@Version :   1.0
@Contact :   raogx.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   
输入
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
输出
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

解释
OrderedStream os= new OrderedStream(5);
os.insert(3, "ccccc"); // 插入 (3, "ccccc")，返回 []
os.insert(1, "aaaaa"); // 插入 (1, "aaaaa")，返回 ["aaaaa"]
os.insert(2, "bbbbb"); // 插入 (2, "bbbbb")，返回 ["bbbbb", "ccccc"]
os.insert(5, "eeeee"); // 插入 (5, "eeeee")，返回 []
os.insert(4, "ddddd"); // 插入 (4, "ddddd")，返回 ["ddddd", "eeeee"]

提示：

1 <= n <= 1000
1 <= id <= n
value.length == 5
value 仅由小写字母组成
每次调用 insert 都会使用一个唯一的 id
恰好调用 n 次 insert


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/design-an-ordered-stream
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List 

class OrderedStream:

    def __init__(self, n: int):
        self.cur_idx = 1
        self.value_list = [None] * 1001

    def insert(self, idKey: int, value: str) -> List[str]:
        self.value_list[idKey] = value 
        res_list = []
        while self.value_list[self.cur_idx]:
            res_list.append(self.value_list[self.cur_idx])
            self.cur_idx += 1
        return res_list



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)