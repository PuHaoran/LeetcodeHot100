"""
309. 最佳买卖股票时机含冷冻期
给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。



示例 1:

输入: prices = [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
示例 2:

输入: prices = [1]
输出: 0
"""
""" 题解
①状态表达。f(i,j)表示第i天j状态下的最大股票收益。
②状态转移。f(i,0)持股状态下的最大收益。
          f(i,1)非持股下一天不在冷冻期的最大收益。
          f(i,2)非持股下一天在冷冻期的最大收益。
f(i,0)=max(f(i-1,0),f(i-1,1)-prices[i])
f(i,1)=max(f(i-1,2),f(i-1,1))
f(i,2)=f(i-1,0)+prices[i]
"""


class Solution:
    def maxProfit(self, prices) -> int:
        f = [[-prices[0], 0, 0] for _ in range(len(prices))]
        for i in range(1, len(prices)):
            f[i][0] = max(f[i-1][0], f[i-1][1]-prices[i])
            f[i][1] = max(f[i-1][1], f[i-1][2])
            f[i][2] = f[i-1][0]+prices[i]
        return max(prices[len(prices)-1])
