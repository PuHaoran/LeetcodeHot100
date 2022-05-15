"""
128. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。



示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""
# 2 3 4 5
# 1 _ 2 1
# 4 4 2 4

""" 题解
用空间换时间，当前元素对应的长度等于左边元素对应的长度+右边元素对应的长度，并更新区间左右端点。
"""


class Solution:
    def longestConsecutive(self, nums):
        res = 0
        d = {}
        for num in nums:
            if num in d:
                continue
            d[num] = 0
            l, r = 0, 0
            if num-1 in d:
                l = d[num-1]
            if num+1 in d:
                r = d[num+1]
            d[num] = l + r + 1
            res = max(res, d[num])
            d[num-l] = d[num]
            d[num+r] = d[num]
        return res


nums = [0,3,7,2,5,8,4,6,0,1]
solution = Solution()
print(solution.longestConsecutive(nums))
