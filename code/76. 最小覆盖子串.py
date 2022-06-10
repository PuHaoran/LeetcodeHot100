"""
76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。



注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。


示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
"""
""" 题解
维持一个从j到i的滑动窗口，每次增加一个元素，若有效则cnt+1，然后判断j对应的元素是否有效，无效则向前移动一位；滑动过程中判断当前元素是否为最小覆盖子串。
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        s_dict, t_dict = collections.defaultdict(int), collections.defaultdict(int)
        for c in t:
            t_dict[c] += 1
        i, j = 0, 0
        res = ''
        cnt = 0
        while i < len(s):
            s_dict[s[i]] += 1
            if s_dict[s[i]] <= t_dict[s[i]]:
                cnt += 1
            while s_dict[s[j]] > t_dict[s[j]]:  # i是否无效
                s_dict[s[j]] -= 1
                j += 1
            print(cnt, i, j)
            if cnt == len(t) and (len(res) == 0 or i-j+1 < len(res)):
                res = s[j:i+1]
            i += 1
        return res


s = "ADOBECODEBANC"
t = "ABCF"
solution = Solution()
print(solution.minWindow(s, t))
