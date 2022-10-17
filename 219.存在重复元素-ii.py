#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
from typing import List 

# @lc code=start
class Solution:
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            s = nums[i:i+k+1]
            n = len(s)
            nn = len(set(s))
            if n != nn:
                return True 
        return False
# @lc code=end

