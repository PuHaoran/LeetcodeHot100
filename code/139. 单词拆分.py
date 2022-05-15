"""
139. 单词拆分
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。



示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
"""
""" 题解
DP。①状态表示。f(i)长度为i的子串s[0:i-1]能否拆分成子串。②状态转移。f(i) = f(j) & check(s[j...i-1])，初始化f[0]=1。
 l e e t c o d e
 1 0 0 0 0 0 0 0 0
 1 0 0 0 1 0 0 0 0
 1 0 0 0 1 0 0 0 1
"""


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        f = [0] * (len(s)+1)
        f[0] = 1
        for i in range(1, len(s)+1):
            for j in range(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = 1
                    break
        return bool(f[len(s)])


s = "leetcode"
wordDict = ["leet", "code"]
solution = Solution()
print(solution.wordBreak(s, wordDict))

# 递归(超时)
# class Solution:
#     def wordBreak(self, s: str, wordDict) -> bool:
#         global res
#         res = False
#         def dfs(path):
#             global res
#             if len(path) > len(s):
#                 return
#             if path == s:
#                 res = True
#                 return
#             if s[:len(path)] != path:
#                 return
#             for i in range(len(wordDict)):
#                 path += wordDict[i]
#                 dfs(path)
#                 path = path[:-len(wordDict[i])]
#         dfs('')
#         return res
