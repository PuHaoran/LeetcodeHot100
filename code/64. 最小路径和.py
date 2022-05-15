"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。



示例 1：


输入：grid =
[[1,3,1],
[1,5,1],
[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12
"""
""" 题解
DP。f(i,j)=min(f(i-1,j), f(i,j-1))+arr(i,j)。
"""


class Solution:
    def minPathSum(self, grid) -> int:
        n, m = len(grid), len(grid[0])
        f = [[float('inf')]*m for _ in range(n)]
        f[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i-1 >= 0:
                    f[i][j] = f[i-1][j]
                if j-1 >= 0:
                    f[i][j] = min(f[i][j], f[i][j-1])
                f[i][j] += grid[i][j]
        return f[n-1][m-1]-grid[0][0]


grid = [[1,3,1],
[1,5,1],
[4,2,1]]
solution = Solution()
print(solution.minPathSum(grid))
