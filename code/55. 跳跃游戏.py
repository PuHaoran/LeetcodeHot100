"""
55. 跳跃游戏
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。



示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
"""
""" 题解
贪心。保存当前所能达到的最远距离，若当前格子索引小于等于最远距离则判断并更新最远距离，否则说明走不到当前格子，不做更新。
最后，判断最远距离是否大于等于最后一个元素索引。
"""


class Solution:
    def canJump(self, nums) -> bool:
        t = 0  # 所能达到的最远距离
        for i in range(len(nums)):
            if t >= i: # 当前格子能够走到
                t = max(t, i+nums[i]) # 更新最新最远距离
        return True if t >= len(nums)-1 else False


# class Solution:
#     def canJump(self, nums) -> bool:
#         if len(nums) == 1:
#             return True
#         mark = [0] * len(nums)
#         mark[0] = 0 if nums[0] == 0 else 1
#         for i in range(len(nums)-1):
#             if mark[i] == 0:
#                 return False
#             for j in range(i+1, i+1+nums[i]):
#                 if j < len(nums):
#                     mark[j] = 1
#         return bool(mark[len(nums)-1])


nums = [1, 0,1,0]
solution = Solution()
print(solution.canJump(nums))
