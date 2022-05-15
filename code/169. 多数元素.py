"""
169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例 1：

输入：[3,2,3]
输出：3
示例 2：

输入：[2,2,1,1,1,2,2]
输出：2
"""
""" 题解
双指针。先排序，然后判断前后双指针对应元素是否相等，若不相等则i+=1，j-=1，否则返回多数元素。
"""


class Solution:
    def majorityElement(self, nums):
        nums = sorted(nums)
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] != nums[j]:
                i += 1
                j -= 1
            else:
                return nums[i]
