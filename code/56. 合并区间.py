"""
56. 合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。



示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""
""" 题解
先排序，然后考虑相邻两区间可能出现的三种情况。
一    |____|
       |_____|
二    |____|
       |__|
三    |____|
         |__|
"""


class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals)
        t = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= t[1]:
                t[1] = max(intervals[i][1], t[1])
            else:
                res.append(t)
                t = intervals[i]
        res.append(t)
        return res
