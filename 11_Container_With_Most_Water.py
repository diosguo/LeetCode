class Solution:
    def maxArea(self, height):
        l = len(height)
        left = 0
        right = l - 1
        area = min(height[0], height[-1]) * (l - 1)
        while left < right:
            print(left,right)
            if height[left] < height[right]:
                t = left
                if t < right:
                    t += 1
                    if min(height[t], height[right]) * (right - t) > area:
                        area = min(height[t], height[right]) * (right - t)
                if t < right:
                    left = t
                else:
                    return area
            else:
                t = right
                if t > left:
                    t -= 1
                    if min(height[t], height[left]) * (t - left) > area:
                        area = min(height[t], height[left]) * (t - left)
                if t > left:
                    right = t
                else:
                    return area
        return area


s = Solution()
a = [1,8,6,2,5,4,8,3,7]
# print(s.maxArea([1,8,6,2,5,4,8,3,7]))
print(s.maxArea([2,3,4,5,18,17,6]))