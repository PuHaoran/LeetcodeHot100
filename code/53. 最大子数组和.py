"""
53. 最大子数组和
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。



示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
"""
""" 题解
DP。①状态表示。f(i)截至到i的连续子数组和最大。②状态转移。f(i)=max(f(i-1)+arr[i],arr[i])。
"""


class Solution:
    def maxSubArray(self, nums):
        nums = [0] + nums
        f = [0]*len(nums)
        for i in range(1, len(nums)):
            f[i] = max(f[i-1]+nums[i], nums[i])
        return max(f[1:])


nums = [-1]
solution = Solution()
print(solution.maxSubArray(nums))
