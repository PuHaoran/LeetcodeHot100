"""
322. 零钱兑换
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。



示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
"""
""" 题解
完全背包问题
f(i,j)=min(f(i-1,j), f(i-1,j-vi)+wi, f(i-1,j-2vi)+2wi, f(i-1,j-3vi)+3wi...)
f(i,j-vi)=min(f(i-1,j-vi), f(i-1,j-2vi)+wi, f(i-1,j-3vi)+2wi, f(i-1,j-3vi)+3wi...) =>
f(i,j)=min(f(i-1,j), f(i,j-vi)+wi)
①f(i)第i个物品凑的满足总金额数<=amount硬币个数。
②f(i,j)=min(f(i-1,j), f(i-1, j-vi)+1)，初始化f(i,0)=0。
"""


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        coins = [0] + coins
        n = len(coins)
        f = [[float('inf')] * (amount+1) for _ in range(n+1)]
        for i in range(len(f)):
            f[i][0] = 0
        for i in range(1, n):
            for j in range(1, amount+1):
                f[i][j] = f[i-1][j]
                if j-coins[i] >= 0:
                    f[i][j] = min(f[i-1][j], f[i][j-coins[i]]+1)
        res = -1 if f[n-1][amount] == float('inf') else f[n-1][amount]
        return res


coins = [2]
amount = 0
solution = Solution()
print(solution.coinChange(coins, amount))
