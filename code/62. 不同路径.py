"""
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？



示例 1：


输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
o o
o o
o o
=>
1 1
1 2
1 3
"""
""" 题解
法一：DFS会超时。
法二：
①状态表达。f(i,j)当前有几种路径。
②状态转移。f(i,j)=f(i-1,j)+f(i,j-1)
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0]*(n+1) for _ in range(m+1)]
        f[1][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if i != 1 or j != 1:
                    f[i][j] = f[i-1][j]+f[i][j-1]
        return f[m][n]


solution = Solution()
print(solution.uniquePaths(3, 2))

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         f = [[0]*n for _ in range(m)]
#         global cnt
#         cnt = 0
#         dx, dy = [1, 0], [0, 1]
#
#         def dfs(i, j):
#             global cnt
#             if i == m-1 and j == n-1:
#                 cnt += 1
#                 return
#             for k in range(2):
#                 x, y = i+dx[k], j+dy[k]
#                 if x >= 0 and x < m and y >= 0 and y < n and not f[x][y]:
#                     f[x][y] = 1
#                     dfs(x, y)
#                     f[x][y] = 0
#         dfs(0, 0)
#         return cnt

