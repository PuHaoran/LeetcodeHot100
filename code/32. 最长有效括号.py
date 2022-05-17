"""
32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。



示例 1：

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"
示例 2：

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
示例 3：

输入：s = ""
输出：0
"""
""" 题解
栈。定义栈只保存正括号。若是正括号直接入栈，是反括号则不断消除栈内元素，若栈空且)则记录索引作为有效括号的st（边界，不包括当前索引）。
注意)要注意两种情况，若消除后栈空则判断i-st，若消除后依旧由元素则判断i-top。
( ) )  (  (  )  )  
    st top   i     res = max(res, i-top)
( ) )  (  (  )  )  
    st top      i  res = max(res, i-st)
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        st = -1
        top = -1
        stack = [0] * 30010
        for i in range(len(s)):
            if s[i] == '(':  # 直接入栈
                top += 1
                stack[top] = i
            else:
                if top == -1:  # 栈空说明当前元素不合法，记录其所在索引
                    st = i
                else:
                    top -= 1
                    if top == -1:  # 消掉括号后栈空，则说明(st, i]之间是有效括号。
                        res = max(res, i-st)
                    else:  # 消掉括号后栈内存在元素，则说明(top, i]之间是有效括号。
                        res = max(res, i-stack[top])
        return res
