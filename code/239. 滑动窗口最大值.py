"""
239. 滑动窗口最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。



示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
""" 题解
维持一个单调递减的队列。若队列头部对应的索引不再滑窗内，则弹出。若当前值比队列尾部元素大，队列尾部一直弹出元素，然后进队列。
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        queue = [0]*100010
        p, q = -1, -1
        res = []
        for i in range(len(nums)):
            if queue[p+1] < i-k+1:
                p += 1
            while p != q and nums[i] > nums[queue[q]]:
                q -= 1
            q += 1
            queue[q] = i
            if i >= k-1:
                res.append(nums[queue[p+1]])
        return res


nums = [1,3,1,2,0,5]
k = 3
solution = Solution()
print(solution.maxSlidingWindow(nums, k))
