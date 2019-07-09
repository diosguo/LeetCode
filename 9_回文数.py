class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        t = x
        a = 0

        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        s = str(x)
        b = len(s) - 1
        while (a < b):
            if s[a] != s[b]:
                return False
            a += 1
            b -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.isPalindrome(121)
    print(r)
