"""
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

子数组 是数组的连续子序列。



示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""
""" 题解
①状态表达。fmax(i)截止到i的最大乘积。fmin(i)截止到i的最小乘积。
②状态转移。fmax(i) = max(fmin(i-1)*a[i], fmax(i-1)*a[i], a[i]);fmin(i) = min(fmin(i-1)*a[i], fmax(i-1)*a[i], a[i])
"""


class Solution:
    def maxProduct(self, nums):
        f_min = [0] * len(nums)
        f_max = [0] * len(nums)
        f_min[0], f_max[0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            f_min[i] = min(f_min[i-1]*nums[i], f_max[i-1]*nums[i], nums[i])
            f_max[i] = max(f_min[i-1]*nums[i], f_max[i-1]*nums[i], nums[i])
        return max(f_max)


nums = [2,3,-2,4]
solution = Solution()
print(solution.maxProduct(nums))
