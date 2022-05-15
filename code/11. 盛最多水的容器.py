"""
11. 盛最多水的容器
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。
"""
""" 题解
双指针。前后双指针，i、j小的元素向里面移动一位。
"""


class Solution:
    def maxArea(self, height):
        i, j = 0, len(height)-1
        res = 0
        while i < j:
            res = max(res, min(height[i], height[j])*(j-i))
            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        return res


height = [1,2,4,3]
solution = Solution()
print(solution.maxArea(height))
