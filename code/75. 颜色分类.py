"""
75. 颜色分类
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库的sort函数的情况下解决这个问题。



示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]
"""
""" 题解
法一：快排。
3 1 2 4 5
i   j
2 1 3 4 5
  j i     
法二：双指针。先排0，再排1。
2 0 2 1 1 0

"""


class Solution:
    def sortColors(self, nums) -> None:
        idx = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        for i in range(idx, len(nums)):
            if nums[i] == 1:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        print(nums)

# class Solution:
#     def sortColors(self, nums) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         def quick_sort(nums, l, r):
#             if l >= r:
#                 return
#             i, j = l-1, r+1
#             x = nums[l]
#             while i < j:
#                 while 1:
#                     i += 1
#                     if nums[i] >= x:
#                         break
#                 while 1:
#                     j -= 1
#                     if nums[j] <= x:
#                         break
#                 if i < j:
#                     nums[i], nums[j] = nums[j], nums[i]
#             quick_sort(nums, l, j)
#             quick_sort(nums, j+1, r)
#         quick_sort(nums, 0, len(nums)-1)
#         return nums
