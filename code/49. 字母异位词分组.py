"""
49. 字母异位词分组
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。



示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]
"""
""" 题解
字符串中字符和字符个数都相同字符串叫做同源字符串。
字典存储排序后的字符串，然后将同源的字符串存储到同一个key下。
"""


class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for s in strs:
            t = ''.join(sorted(s))
            if t not in d:
                d[t] = [s]
            else:
                d[t].append(s)
        return list(d.values())
