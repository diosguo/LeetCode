class Solution:
    def searchRange(self, nums, target: int):
        self.most_left = -1
        self.most_right = -1

        if len(nums)==0:
            return [-1,-1]

        def bi_search(nums, left, right, target, direction):
            if right - left < 0:
                return
            mid = (left + right) // 2

            if direction == 0:
                print(mid, nums[mid])
                if nums[mid] < target:
                    bi_search(nums, mid + 1, right, target, direction)
                elif nums[mid] > target:
                    bi_search(nums, left, mid - 1, target, direction)
                else:
                    self.most_left = mid
                    bi_search(nums, left, mid - 1, target, direction)
            else:
                if nums[mid] < target:
                    bi_search(nums, mid + 1, right, target, direction)
                elif nums[mid] > target:
                    bi_search(nums, left, mid - 1, target, direction)
                else:
                    self.most_right = mid
                    bi_search(nums, mid + 1, right, target, direction)

        bi_search(nums, 0, len(nums) - 1, target, 0)
        bi_search(nums, 0, len(nums) - 1, target, 1)
        return [self.most_left, self.most_right]

s = Solution()
a = [5,7,7,8,8,10]
print(s.searchRange(a,8))