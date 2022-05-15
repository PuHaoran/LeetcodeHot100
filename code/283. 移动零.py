"""
283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。



示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
示例 2:

输入: nums = [0]
输出: [0]
"""
""" 题解
双指针，一个指针指向要放置0的位置，一个指针遍历数组。若当前元素为0则将之后的所有元素前移。
"""


class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        i, j = n, n
        while i >= 0:
            if nums[i] == 0:
                for i in range(i + 1, j + 1):
                    nums[i - 1] = nums[i]
                nums[j] = 0
                j -= 1
            i -= 1
