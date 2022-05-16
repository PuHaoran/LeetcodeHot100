"""
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
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


nums1, nums2 = [1], [2, 3, 4, 5, 6]
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))
