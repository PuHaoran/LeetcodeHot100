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
合并两个数组并排序，然后取中间数或中间两数均值。
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

""" 题解
分治解法。将原问题转化为求两数组第k小的数，然后分别考虑两数组长度和奇偶情况，奇数取中间值，偶数取中间两数均值。
重点是分治法求两数组第k小的数，因为是排过序的，若A的k//2元素小于B的k//2元素，则A的前半部分可以舍弃，原问题变为求k-(k//2)小的数；否则舍弃B的前半部分。
当A数组为空或k=1时递归终止。
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        def find(nums1, i, nums2, j, k):
            """ 从两个数组nums1[i:],nums2[j:]中寻找第k小的数 """
            if len(nums1)-i > len(nums2)-j:
                return find(nums2, j, nums1, i, k)
            # 第一种边界情况，第一个数组为空，则直接返回第二个数组的第k个数
            if i == len(nums1):
                return nums2[j+k-1]
            # 第二种边界情况，寻找第k=1小的数
            if k == 1:
                if len(nums1) == 0:
                    return nums2[j]
                return min(nums1[i], nums2[j])
            si, sj = min(i + k // 2, len(nums1)), j + k - k // 2  # 考虑k奇偶的情况，这里不一定均分
            if nums1[si-1] < nums2[sj-1]:
                return find(nums1, si, nums2, j, k-(si-i))
            else:
                return find(nums1, i, nums2, sj, k-(sj-j))

        cnt = len(nums1) + len(nums2)
        if cnt & 1:
            return find(nums1, 0, nums2, 0, cnt // 2 + 1)
        else:
            l = find(nums1, 0, nums2, 0, cnt // 2)
            r = find(nums1, 0, nums2, 0, cnt // 2 + 1)
            return (l + r) / 2.0
