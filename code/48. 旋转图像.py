"""
48. 旋转图像
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。



示例 1：


输入：matrix =
(0,0)(0,1)
[[1,2,3],(0,2)
[4,5,6],
[7,8,9]]    i->j(0->2) (1->1) (2->0) j=n-1-i
(2,0)       j->i(0->0) (1->1) (2->2) i=j
输出：
(0,0)   (0,2)
[[7,4,1],
[8,5,2],(1,2)
[9,6,3]](2,2)
示例 2：


输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""
""" 题解
先按主对角线翻转，然后左右翻转；或先按副对角线反转，然后上下翻转。
1 2 3
4 5 6
7 8 9
=》先主对角线翻转
1 4 7
2 5 8 
3 6 9
=》再水平翻转
7 4 1
8 5 2
9 6 3
"""


class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[n-i-1][n-j-1] = matrix[n-i-1][n-j-1], matrix[i][j]
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]


matrix = [[1,2,3],
[4,5,6],
[7,8,9]]
solution = Solution()
solution.rotate(matrix)
