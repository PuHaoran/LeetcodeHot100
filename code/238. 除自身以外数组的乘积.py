"""
238. 除自身以外数组的乘积
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请不要使用除法，且在 O(n) 时间复杂度内完成此题。



示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
"""
""" 题解
    1  2  3  4
    1  2  3  4
    1  2  3  4
    1  2  3  4
先从上到下计算下三角，然后从下到上计算上三角。
"""


class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] *= res[i-1]*nums[i-1]
        t = 1
        for i in range(len(nums)-1, 0, -1):
            t *= nums[i]
            res[i-1] *= t
        return res


nums = [-1,1]
solution = Solution()
print(solution.productExceptSelf(nums))
