"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

示例 1:

输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
"""
""" 题解
单调栈。找到矩形最大面积本质是找当前柱子比它低的左右两边所形成的面积，故我们通过单调栈可以找到左右两边left、right第一个比当前元素小的元素;
然后res = max(res, arr[i]*(right[i]-left[i]-1))。
"""


class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        from collections import deque
        res = 0
        q = deque()
        left, right = [0]*n, [0]*n
        for i in range(n):
            while len(q) and heights[i] <= heights[q[-1]]:
                q.pop()
            if len(q) == 0:
                left[i] = -1
            else:
                left[i] = q[-1]
            q.append(i)

        q = deque()
        for i in range(n-1, -1, -1):
            print(i)
            while len(q) and heights[i] <= heights[q[-1]]:
                q.pop()
            if len(q) == 0:
                right[i] = n
            else:
                right[i] = q[-1]
            q.append(i)

        for i in range(n):
            res = max(res, heights[i]*(right[i]-left[i]-1))
        return res
