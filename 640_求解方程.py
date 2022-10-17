"""
求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。

如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。

如果方程中只有一个解，要保证返回值 'x' 是一个整数。

 

示例 1：

输入: equation = "x+5-3+x=6+x-2"
输出: "x=2"
示例 2:

输入: equation = "x=x"
输出: "Infinite solutions"
示例 3:

输入: equation = "2x=x"
输出: "x=0"

提示:

3 <= equation.length <= 1000
equation 只有一个 '='.
equation 方程由整数组成，其绝对值在 [0, 100] 范围内，不含前导零和变量 'x' 。 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/solve-the-equation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def parse_expression(self, expression: str):
        parts = []
        x_parts = []
        sub_part = []
        sign = 1
        for char in expression:
            if char in '+-' and sub_part:
                if 'x' in sub_part:
                    if len(sub_part) == 1:
                        sub_part = ['1', 'x']
                    x_parts.append(sign * int(''.join(sub_part[:-1])))
                else:
                    parts.append(sign * int(''.join(sub_part)))
                sub_part = []
            if char == '+':
                sign = 1
            elif char == '-':
                sign = -1
            else:
                sub_part.append(char)
        if sub_part:
            if 'x' in sub_part:
                if len(sub_part) == 1:
                    sub_part = ['1', 'x']
                x_parts.append(sign * int(''.join(sub_part[:-1])))
            else:
                parts.append(sign * int(''.join(sub_part)))

        return sum(parts), sum(x_parts)

    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        left_constant, left_x = self.parse_expression(left)
        right_constant, right_x = self.parse_expression(right)

        right_value = right_constant - left_constant
        x_value = left_x - right_x

        if x_value == 0 and right_value == 0:
            return 'Infinite solutions'
        elif x_value == 0 and right_value != 0:
            return 'No solution'
        else:
            return 'x='+str(right_value // x_value)



if __name__ == '__main__':
    s = Solution()
    res = s.solveEquation('x=x')
    print(res)
