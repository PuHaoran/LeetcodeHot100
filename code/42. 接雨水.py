"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
"""
""" 题解
     _
    | |    _
    | |_B | |
    | | |A| |  
    |_|_|_|_|
一       last
      top
二     last
    top    
单调栈。若当前高度高于等于栈顶高度（第三个柱），则先计算A区域(height[top]-last)*(i-top-1)。然后当前高度低于栈顶高度，计算B区域(height[i]-last)*(i-top-1)。
"""


class Solution:
    def trap(self, height) -> int:
        res = 0
        from collections import deque
        q = deque()
        for i in range(len(height)):
            last = 0
            while len(q) and height[q[-1]] <= height[i]:
                # 长 * 高
                res += (i-q[-1]-1) * (height[q[-1]]-last)
                last = height[q[-1]]
                q.pop()

            if len(q):
                res += (i-q[-1]-1) * (height[i]-last)
            q.append(i)
        return res


