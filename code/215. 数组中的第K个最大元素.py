"""
215. 数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。



示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
"""
""" 题解
[3 1 2 4 5]
 i   j     
 2 1 3 4 5
   j i
[l, j]
[j+1, r]
"""


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        def quick_sort(nums, l, r, k):
            if l >= r:
                return nums[l]
            x = nums[l]
            i, j = l-1, r+1
            while i < j:
                while 1:
                    i += 1
                    if nums[i] <= x:
                        break
                while 1:
                    j -= 1
                    if nums[j] >= x:
                        break
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            if k <= j-l+1:
                return quick_sort(nums, l, j, k)
            else:
                return quick_sort(nums, j+1, r, k-(j-l+1))
        res = quick_sort(nums, 0, len(nums)-1, k)
        return res


nums = [3,2,3,1,2,4,5,5,6]
k = 4
solution = Solution()
print(solution.findKthLargest(nums, k))
