class Solution:
    def plusOne(self, digits):
        c=0
        start=1
        for i in range(len(digits)-1,-1,-1):
            t = digits[i]+start+c
            if start==1 or c==1:
                if t>=10:
                    t = t-10
                    c=1
                else:
                    c=0
                digits[i] = t
                start=False
            else:
                break
        if c ==1:
            digits = [1]+digits
        return digits

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9]))

