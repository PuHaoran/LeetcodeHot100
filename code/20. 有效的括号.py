"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。


示例 1：

输入：s = "()"
输出：true
示例 2：

输入：s = "()[]{}"
输出：true
示例 3：

输入：s = "(]"
输出：false
示例 4：

输入：s = "([)]"
输出：false
示例 5：

输入：s = "{[]}"
输出：true
"""
""" 题解
栈。从前向后遍历，若为左括号，则直接入栈；若为右括号，则判断是否匹配，若匹配则出栈，不匹配则False。若最后栈不为空则False。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        t = -1
        stack = [0] * 10010
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in ['(', '[', '{']:
                t += 1
                stack[t] = c
            else:
                if t != -1 and stack[t] == d[c]:
                    t -= 1
                else:
                    return False
        if t == -1:
            return True
        return False


s = "()[{}"
solution = Solution()
print(solution.isValid(s))
