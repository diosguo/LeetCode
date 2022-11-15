#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   665_非递减数列.py
@Time    :   2022/11/16 00:26:46
@Author  :   DiosGuo 
@Version :   1.0
@Contact :   raogx.vip@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

from typing import List 

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:

        if len(nums) <= 2:
            return True 
        
        near_match_cnt = 0 
        match_idx = None 
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                near_match_cnt += 1
                match_idx = i
        if near_match_cnt == 0:
            return True 
        elif near_match_cnt > 1:
            return False 

        nums[match_idx-1] < nums[match_idx+1]