class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        res = 0
        sign = 1
        if dividend * divisor < 0:
            sign = -1
        if dividend == 0:
            return 0
        divide = abs(dividend)
        divisor = abs(divisor)
        while True:
            k=0
            for k in range(32):
                if 2**k * divisor > divide:
                    break
            # print('k=%d'%k)
            if k == 0:
                break
            else:
                res += 2**(k-1)
                divide -= 2**(k-1)*divisor
            # print('res=%d'%res)
        res = sign * res
        if res>2**31-1:
            res = 2**31-1
        if res<-2**31:
            res = -2**31
        return res


s = Solution()
print(s.divide(-2147483648, 1))
print(2**0)
