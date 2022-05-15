"""
448. 找到所有数组中消失的数字
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。



示例 1：

输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]
示例 2：

输入：nums = [1,1]
输出：[2]
"""
""" 题解
4 3 2 7 8 2 3 1
=>
-4 -3 -2 -7 8 2 -3 -1
出现过得坑位就加上符号，最后没有符号的就是未出现的。
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        for num in nums:
            nums[abs(num)-1] = -abs(nums[abs(num)-1])
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
