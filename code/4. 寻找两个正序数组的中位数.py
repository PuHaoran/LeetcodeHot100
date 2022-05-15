"""
4. 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
"""
""" 题解
法一合并两个数组并排序，然后取中间数或中间两数均值。
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        i, j = 0, 0
        arr = []
        while i < m or j < n:
            if i < m and j < n:
                if nums1[i] < nums2[j]:
                    arr.append(nums1[i])
                    i += 1
                else:
                    arr.append(nums2[j])
                    j += 1
            elif i < m:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
        return arr[len(arr)//2] if len(arr) % 2 else (arr[len(arr)//2-1]+arr[len(arr)//2])/2.0


nums1 = []
nums2 = []
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))
