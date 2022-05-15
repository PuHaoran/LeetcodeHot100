"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？


示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
"""
""" 题解
二分。找开始和结束节点即找右区间端点和左区间端点。
"""


class Solution:
    def searchRange(self, nums, target: int):
        def bin_search1(nums, target, l, r):
            if l >= r:
                if target == nums[l]:
                    return l
                else:
                    return -1
            mid = (l+r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
            return bin_search1(nums, target, l, r)

        def bin_search2(nums, target, l, r):
            if l >= r:
                if target == nums[l]:
                    return l
                else:
                    return -1
            mid = (l+r+1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
            return bin_search2(nums, target, l, r)
        if len(nums) == 0:
            return [-1, -1]
        return bin_search1(nums, target, 0, len(nums)-1), bin_search2(nums, target, 0, len(nums)-1)


target = 8
nums = [5,7,7,8,8,10]
solution = Solution()
print(solution.searchRange(target=target, nums=nums))
