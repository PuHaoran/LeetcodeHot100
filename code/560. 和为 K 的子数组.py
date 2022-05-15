"""
560. 和为 K 的子数组
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数。



示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

0 1 2 3

输入：nums = [1,2,3], k = 3
输出：2
"""
""" 题解
前缀和。先求前缀和，然后转化为区间和等于k的个数的问题，即当前前缀和-之前前缀和==k的个数，之前前缀和出现次数用字典存储。
"""


class Solution:
    def subarraySum(self, nums, k: int):
        res = 0
        nums = [0]+nums
        f = [0] * len(nums)
        for i in range(1, len(nums)):
            f[i] = f[i-1] + nums[i]
        d = {}
        d[0] = 1
        for i in range(1, len(f)):
            if f[i]-k in d:
                res += d[f[i]-k]
            if f[i] not in d:
                d[f[i]] = 0
            d[f[i]] += 1
        return res


nums = [1,2,3]
k = 3
solution = Solution()
print(solution.subarraySum(nums, k))


# class Solution:
#     def subarraySum(self, nums, k: int):
        # res = 0
        # n = len(nums)
        # for i in range(n):
        #     s = 0
        #     for j in range(i, n):
        #         s += nums[j]
        #         if s == k:
        #             res += 1
        # return res
