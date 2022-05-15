"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。



示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
"""
""" 题解
DFS+剪枝。u为递归函数终止条件，mark数组记录正反括号次数，若(数量<)数量则提前终止递归，遍历所有可能条件，递归并回溯。
"""


class Solution:
    def generateParenthesis(self, n: int):
        arr = ['(', ')']
        res = []
        t = []
        mark = [0, 0]

        def dfs(u):
            # 剪枝
            if mark[1] > mark[0]:
                return
            if u == n*2:
                if mark[0] == mark[1]:
                    res.append(''.join(t))
                return
            for i in range(len(arr)):
                t.append(arr[i])
                mark[i] += 1
                dfs(u+1)
                mark[i] -= 1
                t.pop()

        dfs(0)
        return res


n = 8
solution = Solution()
print(solution.generateParenthesis(n))
