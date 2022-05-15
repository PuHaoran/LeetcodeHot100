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
DFS。一般u代表当前走了多少步，每一步可选择所有[1,2,3]所有情况；本题应该以当前索引之后的所有未便利元素入数组，故u为i。
"""


class Solution:
    def subsets(self, nums):
        global t
        res = []
        t = []
        mark = [0]*len(nums)
        def dfs(u):
            global t
            res.append(t.copy())
            for i in range(u, len(nums)):
                if not mark[i]:
                    mark[i] = 1
                    t.append(nums[i])
                    dfs(i)
                    t.pop()
                    mark[i] = 0
        dfs(0)
        return res


nums = [1, 2, 3]
solution = Solution()
print(solution.subsets(nums))
