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
DFS+剪枝。u为递归函数终止条件，mark数组记录正反括号次数，若正括号数量<反括号数量或正括号数量>最大数量n则提前终止递归，遍历所有可能条件，递归并回溯。
"""


class Solution:
    def generateParenthesis(self, n: int):
        res, temp = [], []
        arr = ['(', ')']
        cnt = [0, 0]

        def dfs(u):
            # 剪枝
            if cnt[1] > cnt[0] or cnt[0] > n:
                return
            if u == 2*n:
                res.append(''.join(temp))
                return
            for i in range(len(arr)):
                temp.append(arr[i])
                cnt[i] += 1
                dfs(u+1)
                cnt[i] -= 1
                temp.pop()
        dfs(0)
        return res


n = 8
solution = Solution()
print(solution.generateParenthesis(n))
