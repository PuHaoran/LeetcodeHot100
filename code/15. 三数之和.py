"""
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]
"""
""" 题解
排序+双指针。从前向后遍历数组，第一个元素为i，终点为j。若item+nums[i]+nums[j]>0，则j--；若item+nums[i]+nums[j]<0，则i++。
"""


class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        n = len(nums)-1
        res = []
        for k in range(len(nums)):
            if nums[k] > 0:
                continue
            i, j = k+1, n
            while i < j:
                if nums[k] + nums[i] + nums[j] == 0:
                    if [nums[k], nums[i], nums[j]] not in res:
                        res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                elif nums[k] + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    i += 1
        return res


nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
solution = Solution()
print(solution.threeSum(nums))
