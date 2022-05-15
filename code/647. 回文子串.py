"""
647. 回文子串
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

回文字符串 是正着读和倒过来读一样的字符串。

子字符串 是字符串中的由连续字符组成的一个序列。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。



示例 1：

输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
"""
""" 题解
遍历数组，从i、j(i/i+1)向两边扩散，若相等则cnt+=1，否则遍历数组。
 a b b c
   i j 
 a b b c
  ij
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(s, i, j):
            n = len(s)-1
            cnt = 0
            while i >= 0 and j <= n:
                if s[i] != s[j]:
                    break
                cnt += 1
                i -= 1
                j += 1
            return cnt
        res = 0
        for i in range(len(s)):
            res += check(s, i, i)
            res += check(s, i, i+1)
        return res


# 暴力遍历
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         def check_s(s):
#             i, j = 0, len(s)-1
#             while i < j:
#                 if s[i] != s[j]:
#                     return False
#                 i += 1
#                 j -= 1
#             return True
#         cnt = 0
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if check_s(s[i: j+1]):
#                     cnt += 1
#         return cnt


s = "fdsklf"
solution = Solution()
print(solution.countSubstrings(s))
