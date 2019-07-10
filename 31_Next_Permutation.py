class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_t = None
        min_off = 9999999
        min_index = 0
        for i in range(len(nums)-1):
            if nums[i] < nums[i + 1]:
                # 顺 序
                last_t = i
            if last_t is not None:
                if min_index < last_t:
                    min_off = 99990
                if 0 < nums[i] - nums[last_t] < min_off:
                    min_index = i
                    min_off = nums[i] - nums[last_t]

        print(last_t, min_index)
        if last_t is None:
            nums[:] = nums[::-1]
            return
        else:
            if 0 < nums[-1] - nums[last_t] < min_off:
                min_index = len(nums) - 1
                min_off = nums[i] - nums[last_t]
            nums[last_t], nums[min_index] = nums[min_index], nums[last_t]


            nums[last_t+1:] = sorted(nums[last_t+1:])



s = Solution()
a =[1,2,0,3,0,1,2,4]
s.nextPermutation(a)
print(a)
# print(a[0:2])
# print(a[1:None:-1])