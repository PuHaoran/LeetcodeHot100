"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
"""
""" 题解
当前(i,i)和(i,i+1)节点向两边扩散，找到对称的子串。
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = list(s)
        res = []
        def get_substr(s, i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i+1:j]

        for i in range(len(s)):
            s1 = get_substr(s, i, i)
            s2 = get_substr(s, i, i+1)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return ''.join(res)


s = "cbbd"
solution = Solution()
print(solution.longestPalindrome(s))
