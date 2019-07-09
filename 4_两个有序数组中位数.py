class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        start1, end1 = 0, len(nums1)
        start2, end2 = 0, len(nums2)

        pos_sum = end1 + end2 - 1 if (end1 + end2) % 2 == 0 else end1 + end2

        # 如果是偶数，那么i1+i2=end1+end2-1
        # 如果是奇数，那么i1+i2=end1+end2

        i1 = end1 // 2
        i2 = pos_sum - end1 - i1

        while start1 < end1 and start2 < end2:
            print(i1,i2)
            if nums1[i1] == nums2[i2]:
                return nums1[i1]
            if nums1[i1] < nums2[i2]:
                start1 = i1 + 1
                end2 = i2 - 1
                if start1 >= end1:
                    break
                i1 = (start1 + end1) // 2
                i2 = pos_sum - len(nums1) - i1
            if nums1[i1] > nums2[i2]:
                end1 = i1 - 1
                start2 = i2 + 1
                i1 = (start1 + end1) // 2
                i2 = pos_sum - len(nums1) - i1

        return nums1[i1]


s = Solution()
res = s.findMedianSortedArrays([1,3],[2])
print(res)