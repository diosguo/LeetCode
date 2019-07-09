class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) < 1:
            return ''
        max_length =10000
        for i in strs:
            if len(i) < max_length:
                max_length = len(i)
        strs.sort()
        for i in range(max_length):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0][:max_length]

if __name__ == '__main__':
    s = Solution()
    res = s.longestCommonPrefix(["flower","flow","flight"])
    print(res)
    res = s.longestCommonPrefix(["dog","racecar","car"])
    print(res)