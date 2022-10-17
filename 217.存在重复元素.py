#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums) 
        nn = len(set(nums))

        return n!=nn
# @lc code=end

