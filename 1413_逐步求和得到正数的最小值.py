from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_acc = nums[0]
        acc = nums[0]
        for i in nums[1:]:
            acc += i
            if acc < min_acc:
                min_acc = acc

                print(min_acc)

        res = 1 - min_acc
        return max(res, 1)


if __name__ == '__main__':
    inp = [-3, 2, -3, 4, 2]

    s = Solution()

    print('=', s.minStartValue(inp))
