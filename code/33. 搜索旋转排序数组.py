"""
33. 搜索旋转排序数组
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。



示例 1：

输入：nums = [4,5,6,7,0,1,2], target = 1
输出：4
示例 2：

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：

输入：nums = [1], target = 0
输出：-1
"""
""" 题解
二分。有序或部分有序数组，要考虑使用二分搜索。在有序区间使用二分，无序区间继续查找。
"""


class Solution:
    def search(self, nums, target):
        def bin_search(nums, target, l, r):
            if l >= r:
                if nums[l] == target:
                    return l
                else:
                    return -1
            mid = (l+r) // 2
            if nums[l] <= nums[mid]:
                if nums[l] <= target and target <= nums[mid]:
                    r = mid
                else:
                    l = mid+1
            else:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid
                else:
                    r = mid-1
            return bin_search(nums, target, l, r)
        return bin_search(nums, target, 0, len(nums)-1)


nums = [0, 1]
target = 0
solution = Solution()
print(solution.search(nums, target))
