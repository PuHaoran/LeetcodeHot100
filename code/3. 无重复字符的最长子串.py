"""
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""
""" 题解
双向队列。通过一个双向队列保存窗口内无重复字符的子序列。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        res = 0
        q = deque()
        s = list(s)
        for i in range(len(s)):
            if s[i] in q:
                res = max(res, len(q))
                while 1:
                    t = q.popleft()
                    if t == s[i]:
                        break
            q.append(s[i])
        res = max(res, len(q))
        return res


s = "pwwkew"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))
