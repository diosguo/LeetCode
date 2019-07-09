class Solution:
    def isValid(self, s: 'str') -> 'bool':
        if s == '':
            return True
        brackets_pairs = {'}': '{', ')': '(', ']': '['}
        stack = list()
        for c in s:
            if c not in brackets_pairs:
                stack.append(c)
            else:
                if len(stack) > 0 and stack[-1] == brackets_pairs.get(c):
                    del stack[-1]
                else:
                    return False

        return len(stack) == 0

s = Solution()
print(s.isValid('(])'))

