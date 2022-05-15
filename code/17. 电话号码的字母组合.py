"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。





示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
"""
""" 题解
DFS。数组mark标记走过的路，dfs函数传递u作为递归终止条件，遍历当前u步的所有可能，临时变量t保存路径并mark=1，递归并回溯。
"""


class Solution:
    def letterCombinations(self, digits: str):
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        mark = [[0]*4 for _ in range(4)]
        res = []
        t = []
        digits = list(digits)
        if len(digits) == 0:
            return res
        def dfs(u):
            if u == len(digits):
                res.append(''.join(t))
                return
            c = digits[u]
            for i in range(len(d[c])):
                if not mark[u][i]:
                    mark[u][i] = 1
                    t.append(d[c][i])
                    dfs(u+1)
                    t.pop()
                    mark[u][i] = 0
        dfs(0)
        return res


digits = ''
solution = Solution()
print(solution.letterCombinations(digits))
