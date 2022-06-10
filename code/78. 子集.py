"""
78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
"""
""" 题解
DFS。dfs包含放nums[u]元素和不放nums[u]元素两种情况，递归终止条件是u=len(nums)。
"""


class Solution:
    def subsets(self, nums):
        global n
        n = len(nums)
        res, t = [], []
        def dfs(u):
            global n
            if u == n:
                res.append(t.copy())
                return
            # 不放
            dfs(u+1)
            # 放
            t.append(nums[u])
            dfs(u+1)
            t.pop()
        dfs(0)
        return res
