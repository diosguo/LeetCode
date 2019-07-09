class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        max_start = 0
        max_end = 0
        max = 0
        for k,i in enumerate(nums):
            if max ==0 and i <=0 :
                continue
            elif max == 0:
                max_start = k
                max = k
            else:
                max += i



        pass

s = Solution()
t = s.maxSubArray()
print(t)