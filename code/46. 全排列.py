"""
46. 全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。



示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]
"""
""" 题解
DFS。u作为递归终止条件。遍历所有可能条件，递归并回溯。
"""


class Solution:
    def permute(self, nums):
        n = len(nums)
        mark = [0] * n
        global t, res
        res, t = [], []
        def dfs(u):
            if u == n:
                res.append(t.copy())
                return
            for i in range(n):
                if not mark[i]:
                    t.append(nums[i])
                    mark[i] = 1
                    dfs(u+1)
                    t.pop()
                    mark[i] = 0
        dfs(0)
        return res


nums = [1,2,3]
solution = Solution()
print(solution.permute(nums))
