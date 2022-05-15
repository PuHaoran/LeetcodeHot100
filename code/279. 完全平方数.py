"""
279. 完全平方数
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。



示例 1：

输入：n = 12
输出：3
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9
"""
""" 题解
①f(i)当前i完全平方数的最少数量。
②f(i) = min(f(i), f(i-j*j))（i-j*j>=0）。
1 2 3 4 5 6 7 8 9 10 11 12 
1 2 3 1 2 3 4 2 1 2  3  3
"""


class Solution:
    def numSquares(self, n: int) -> int:
        f = [0] * 10010
        for i in range(1, n+1):
            f[i] = f[i-1]+1
            j = 1
            while i-j*j>=0:
                f[i] = min(f[i], f[i-j*j]+1)
                j += 1
        return f[n]


n = 12
solution = Solution()
print(solution.numSquares(n))
