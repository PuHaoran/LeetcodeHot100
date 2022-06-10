"""
79. 单词搜索
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。



示例 1：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
"""
""" 题解
DFS。dfs中首先判断不满足的条件，然后搜索所有可能性，res=dfs() or dfs() return res。
"""


class Solution:
    def exist(self, board, word: str) -> bool:
        global m, n, flag
        m, n = len(board), len(board[0])
        mark = [[0]*n for _ in range(m)]

        def dfs(i, j, u):
            global m, n, flag
            # 终止条件
            if u == len(word):
                flag = 1
                return True
            # 不满足条件的
            if i < 0 or i > m-1 or j < 0 or j > n-1 or mark[i][j] or board[i][j] != word[u]:
                return
            dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
            for k in range(4):
                x, y = i+dx[k], j+dy[k]
                mark[i][j] = 1
                dfs(x, y, u+1)
                mark[i][j] = 0

        flag = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, 0)
                if flag:
                    return True
        return False


board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
word = "AAB"
solution = Solution()
print(solution.exist(board, word))
